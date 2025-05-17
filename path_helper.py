#!/usr/bin/env python
"""
Path Helper for Cross-Environment Development

This module provides functionality to handle path differences between
Windows and Ubuntu environments in the CCDE project.
"""

import os
import sys
import platform
import json
from pathlib import Path


class PathHelper:
    """Handles path resolution across different environments."""

    def __init__(self):
        """Initialize the path helper."""
        self.is_windows = platform.system() == "Windows"
        self.env_file = self._get_env_file()
        self.env_vars = self._load_env_vars()
        self.repo_root = self._get_repo_root()

    def _get_env_file(self):
        """Determine which environment file to use based on the platform."""
        if self.is_windows:
            return "env-windows.txt"
        else:
            return "env-ubuntu.txt"

    def _load_env_vars(self):
        """Load environment variables from the appropriate env file."""
        env_vars = {}
        try:
            # Start with script directory
            script_dir = Path(__file__).parent.absolute()

            # Try to find env file in script directory
            env_path = script_dir / self.env_file

            # If not found, look in parent directories
            if not env_path.exists():
                for parent in script_dir.parents:
                    env_path = parent / self.env_file
                    if env_path.exists():
                        break

            # If still not found, use default locations
            if not env_path.exists():
                if self.is_windows:
                    env_path = Path(
                        "C:/Users/kiman/Documents/GitHub/CCDE_Cisco") / self.env_file
                else:
                    env_path = Path(
                        "/home/kimanduw/CCDE_Cisco") / self.env_file

            # Read and parse the env file if it exists
            if env_path.exists():
                with open(env_path, "r") as f:
                    for line in f:
                        line = line.strip()
                        # Skip comments and empty lines
                        if not line or line.startswith("#"):
                            continue

                        # Parse key-value pairs
                        if "=" in line:
                            key, value = line.split("=", 1)
                            # Handle variable substitution
                            while "${" in value and "}" in value:
                                start = value.find("${")
                                end = value.find("}", start)
                                var_name = value[start+2:end]
                                if var_name in env_vars:
                                    value = value[:start] + \
                                        env_vars[var_name] + value[end+1:]
                                else:
                                    break
                            env_vars[key] = value

            return env_vars
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            return {}

    def _get_repo_root(self):
        """Get the repository root path."""
        if "REPO_ROOT" in self.env_vars:
            return Path(self.env_vars["REPO_ROOT"])

        # Try to detect using git
        try:
            import subprocess
            result = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                return Path(result.stdout.strip())
        except:
            pass

        # Default fallback paths
        if self.is_windows:
            return Path("C:/Users/kiman/Documents/GitHub/CCDE_Cisco")
        else:
            return Path("/home/kimanduw/CCDE_Cisco")

    def get_path(self, relative_path):
        """
        Get an absolute path from a path relative to the repo root.

        Args:
            relative_path: Path relative to repository root

        Returns:
            Absolute path as a Path object
        """
        return self.repo_root / Path(relative_path)

    def get_data_path(self, relative_path=""):
        """Get a path within the data directory."""
        if "DATA_PATH" in self.env_vars:
            data_path = Path(self.env_vars["DATA_PATH"])
        else:
            data_path = self.repo_root / "data"

        if relative_path:
            return data_path / Path(relative_path)
        return data_path

    def get_storage_path(self, relative_path=""):
        """Get a path within the storage directory."""
        if "STORAGE_PATH" in self.env_vars:
            storage_path = Path(self.env_vars["STORAGE_PATH"])
        else:
            storage_path = self.repo_root / "storage"

        if relative_path:
            return storage_path / Path(relative_path)
        return storage_path

    def get_log_path(self, relative_path=""):
        """Get a path within the log directory."""
        if "LOG_PATH" in self.env_vars:
            log_path = Path(self.env_vars["LOG_PATH"])
        else:
            log_path = self.repo_root / "logs"

        if relative_path:
            return log_path / Path(relative_path)
        return log_path

    def get_python_path(self):
        """Get the Python executable path."""
        if "PYTHON_PATH" in self.env_vars:
            return self.env_vars["PYTHON_PATH"]

        return sys.executable

    def get_env_info(self):
        """Get information about the current environment."""
        return {
            "platform": platform.system(),
            "is_windows": self.is_windows,
            "env_file": str(self.env_file),
            "repo_root": str(self.repo_root),
            "env_vars": self.env_vars
        }

    def print_env_info(self):
        """Print environment information."""
        info = self.get_env_info()
        print(json.dumps(info, indent=2))


if __name__ == "__main__":
    # When run directly, print environment information
    helper = PathHelper()
    helper.print_env_info()

    # Print some example paths
    print("\nExample Paths:")
    print(f"Repo Root: {helper.repo_root}")
    print(f"Data Path: {helper.get_data_path()}")
    print(f"Storage Path: {helper.get_storage_path()}")
    print(f"Log Path: {helper.get_log_path()}")
    print(f"Python Path: {helper.get_python_path()}")

    # If arguments provided, resolve those paths
    if len(sys.argv) > 1:
        print("\nResolved Paths:")
        for path in sys.argv[1:]:
            print(f"{path} -> {helper.get_path(path)}")
