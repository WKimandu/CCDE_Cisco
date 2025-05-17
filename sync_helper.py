#!/usr/bin/env python
"""
Sync Helper for Multi-Environment Development

This script provides utilities to synchronize the repository between
Windows and Ubuntu environments using both Git and direct file transfer.
"""

import os
import sys
import argparse
import platform
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Import PathHelper from path_helper.py
try:
    from path_helper import PathHelper
except ImportError:
    # If running from a different directory, try to import relative to this script
    script_dir = Path(__file__).parent.absolute()
    sys.path.append(str(script_dir))
    from path_helper import PathHelper


class SyncHelper:
    """Helps sync repository between Windows and Ubuntu environments."""

    def __init__(self):
        """Initialize the sync helper."""
        self.path_helper = PathHelper()
        self.is_windows = platform.system() == "Windows"
        self.env_vars = self.path_helper.env_vars
        self.repo_root = self.path_helper.repo_root

    def _run_command(self, command, cwd=None, shell=False):
        """Run a shell command and return the result."""
        if cwd is None:
            cwd = self.repo_root

        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=cwd,
                shell=shell
            )
            return result
        except Exception as e:
            print(f"Error running command: {e}")
            return None

    def get_git_status(self):
        """Get the current Git status."""
        result = self._run_command(["git", "status", "--porcelain"])
        if result and result.returncode == 0:
            changes = [line for line in result.stdout.split("\n") if line]
            return changes
        return []

    def get_current_branch(self):
        """Get the current Git branch."""
        result = self._run_command(["git", "branch", "--show-current"])
        if result and result.returncode == 0:
            return result.stdout.strip()
        return "unknown"

    def get_remote_info(self):
        """Get information about the remote repository."""
        result = self._run_command(["git", "remote", "-v"])
        remotes = {}

        if result and result.returncode == 0:
            for line in result.stdout.split("\n"):
                if not line:
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    name, url = parts[0], parts[1]
                    remotes[name] = url

        return remotes

    def push_to_remote(self, remote="origin", branch=None):
        """Push changes to the remote repository."""
        if branch is None:
            branch = self.get_current_branch()

        print(f"Pushing to {remote}/{branch}...")
        result = self._run_command(["git", "push", remote, branch])

        if result:
            print(result.stdout)
            if result.stderr:
                print(result.stderr)

            return result.returncode == 0

        return False

    def pull_from_remote(self, remote="origin", branch=None):
        """Pull changes from the remote repository."""
        if branch is None:
            branch = self.get_current_branch()

        print(f"Pulling from {remote}/{branch}...")
        result = self._run_command(["git", "pull", remote, branch])

        if result:
            print(result.stdout)
            if result.stderr:
                print(result.stderr)

            return result.returncode == 0

        return False

    def sync_to_other_env(self):
        """Sync changes to the other environment using file transfer."""
        if "REMOTE_HOST" not in self.env_vars or "REMOTE_USERNAME" not in self.env_vars or "REMOTE_PATH" not in self.env_vars:
            print("Error: Remote server details not found in environment configuration")
            return False

        remote_host = self.env_vars["REMOTE_HOST"]
        remote_username = self.env_vars["REMOTE_USERNAME"]
        remote_path = self.env_vars["REMOTE_PATH"]

        print(f"Syncing to {remote_username}@{remote_host}:{remote_path}...")

        if self.is_windows:
            # Sync from Windows to Ubuntu
            command = [
                "scp", "-r",
                str(self.repo_root / "*"),
                f"{remote_username}@{remote_host}:{remote_path}"
            ]
        else:
            # Sync from Ubuntu to Windows
            command = [
                "scp", "-r",
                str(self.repo_root / "*"),
                f"{remote_username}@{remote_host}:{remote_path}"
            ]

        print(f"Running: {' '.join(command)}")
        result = self._run_command(command)

        if result:
            print(result.stdout)
            if result.stderr:
                print(result.stderr)

            return result.returncode == 0

        return False

    def create_sync_log(self, sync_type, success, message=""):
        """Create a log entry for sync operations."""
        log_dir = self.path_helper.get_log_path()
        os.makedirs(log_dir, exist_ok=True)

        log_file = log_dir / "sync_log.json"

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": sync_type,
            "success": success,
            "environment": "windows" if self.is_windows else "ubuntu",
            "branch": self.get_current_branch(),
            "message": message
        }

        existing_logs = []
        if log_file.exists():
            try:
                with open(log_file, "r") as f:
                    existing_logs = json.load(f)
            except:
                pass

        existing_logs.append(log_entry)

        with open(log_file, "w") as f:
            json.dump(existing_logs, f, indent=2)

    def print_sync_status(self):
        """Print the current status of synchronization."""
        print("\n=== Git Status ===")
        changes = self.get_git_status()
        if changes:
            print("Uncommitted changes:")
            for change in changes:
                print(f"  {change}")
        else:
            print("No uncommitted changes")

        print("\n=== Branch Info ===")
        current_branch = self.get_current_branch()
        print(f"Current branch: {current_branch}")

        print("\n=== Remote Info ===")
        remotes = self.get_remote_info()
        if remotes:
            for name, url in remotes.items():
                print(f"Remote {name}: {url}")
        else:
            print("No remotes configured")

        print("\n=== Environment Info ===")
        self.path_helper.print_env_info()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Sync Helper for Multi-Environment Development")

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show sync status"
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push changes to remote repository"
    )
    parser.add_argument(
        "--pull",
        action="store_true",
        help="Pull changes from remote repository"
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Sync changes to other environment using file transfer"
    )
    parser.add_argument(
        "--remote",
        type=str,
        default="origin",
        help="Remote repository name (default: origin)"
    )
    parser.add_argument(
        "--branch",
        type=str,
        help="Branch name (default: current branch)"
    )

    args = parser.parse_args()

    # If no arguments provided, show status by default
    if not (args.status or args.push or args.pull or args.sync):
        args.status = True

    sync_helper = SyncHelper()

    if args.status:
        sync_helper.print_sync_status()

    if args.push:
        success = sync_helper.push_to_remote(args.remote, args.branch)
        sync_helper.create_sync_log("push", success)

    if args.pull:
        success = sync_helper.pull_from_remote(args.remote, args.branch)
        sync_helper.create_sync_log("pull", success)

    if args.sync:
        success = sync_helper.sync_to_other_env()
        sync_helper.create_sync_log("file_sync", success)


if __name__ == "__main__":
    main()
