# GitOps Workflow for Multi-Environment Development

This document defines the GitOps workflow for synchronized development between Windows and Ubuntu environments.

## Environments

1. **Windows 11 (Primary Development)**
   - Location: `C:\Users\kiman\Documents\GitHub\CCDE_Cisco`
   - Purpose: Main development, UI work, documentation

2. **Ubuntu Server (Secondary Development)**
   - Location: `/home/kimanduw/Documents/CCDE_Cisco` (corrected path)
   - Purpose: Backend development, integration testing, deployment testing

## Branch Strategy

- **main**: Production-ready code
- **develop**: Integration branch for feature work
- **feature/name**: Feature-specific branches
- **env/windows**: Windows-specific changes
- **env/ubuntu**: Ubuntu-specific changes
- **gitops-learning**: Branch for experimenting with GitOps workflows

## Workflow Rules

1. **Synchronization Protocol**
   - Push completed work before ending a session
   - Pull latest changes before starting new work
   - Use `git push -u origin [branch-name]` for new branches

2. **Conflict Resolution Strategy**
   - Prefer local when correct: `git checkout --ours [file]`
   - Prefer remote when correct: `git checkout --theirs [file]`
   - Manual merging for complex conflicts

3. **Environment-Specific Files**
   - Store environment configs in `.env.windows` and `.env.ubuntu`
   - Use `.gitignore` to exclude environment-specific temporary files
   - Use conditional includes in scripts to handle path differences

## Automation Setup

### Git Hooks

#### Pre-Commit Hook
```bash
#!/bin/bash
# Check for environment-specific hardcoded paths
if grep -r "C:\\Users\\kiman" --include="*.py" --include="*.md" .; then
  echo "ERROR: Windows-specific paths found. Use relative paths instead."
  exit 1
fi

# Check for large binary files
if git diff --cached --name-only | xargs ls -l | awk '{print $5}' | grep -q '[0-9]\{7,\}'; then
  echo "WARNING: Large files detected. Consider using Git LFS."
fi
```

#### Pre-Push Hook
```bash
#!/bin/bash
# Run tests before pushing
echo "Running tests before push..."
python -m unittest discover
if [ $? -ne 0 ]; then
  echo "Tests failed. Aborting push."
  exit 1
fi
```

## Synchronization Commands

### From Windows to Ubuntu
```bash
# Push changes from Windows
git push origin [branch-name]

# On Ubuntu
git pull origin [branch-name]
```

### From Ubuntu to Windows
```bash
# Push changes from Ubuntu
git push origin [branch-name]

# On Windows
git pull origin [branch-name]
```

## Maintenance Tasks

1. **Weekly Cleanup**
   ```bash
   git fetch --prune  # Remove references to deleted remote branches
   git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D  # Delete local branches whose remotes are gone
   ```

2. **Repository Health Check**
   ```bash
   git fsck --full  # Check repository integrity
   git gc --aggressive  # Optimize repository storage
   ```

## Learning Exercises

1. **Create Feature Branch**: Create a feature branch on Windows, make changes, push to origin
2. **Pull on Ubuntu**: Pull the feature branch on Ubuntu, make additional changes
3. **Create Conflict**: Make conflicting changes on both systems, practice resolving
4. **Use Stash**: Practice stashing changes when switching contexts
5. **Cherry-Pick**: Apply specific commits across branches 