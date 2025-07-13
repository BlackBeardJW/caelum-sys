"""
Git integration plugin for version control operations and repository management.
"""

from caelum_sys.registry import register_command
import subprocess
import os

def _run_git_command(command):
    """Helper function to run git commands safely."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=os.getcwd()
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return False, "", str(e)

@register_command("git status", safe=True)
def git_status():
    """Get the current git repository status."""
    success, stdout, stderr = _run_git_command("git status --porcelain")
    
    if not success:
        return f"❌ Git error: {stderr or 'Not a git repository or git not installed'}"
    
    if not stdout:
        return "✅ Working directory clean - no changes to commit"
    
    lines = stdout.split('\n')
    modified = [line[3:] for line in lines if line.startswith(' M')]
    added = [line[3:] for line in lines if line.startswith('A ')]
    untracked = [line[3:] for line in lines if line.startswith('??')]
    deleted = [line[3:] for line in lines if line.startswith(' D')]
    
    status_parts = []
    if modified:
        status_parts.append(f"Modified: {len(modified)} files")
    if added:
        status_parts.append(f"Added: {len(added)} files")
    if untracked:
        status_parts.append(f"Untracked: {len(untracked)} files")
    if deleted:
        status_parts.append(f"Deleted: {len(deleted)} files")
    
    return f"📊 Git status: {', '.join(status_parts)}"

@register_command("git add all files", safe=False)
def git_add_all():
    """Add all changes to git staging area."""
    success, stdout, stderr = _run_git_command("git add .")
    
    if success:
        return "✅ All changes added to staging area"
    else:
        return f"❌ Git add failed: {stderr}"

@register_command("git commit with message {message}", safe=False)
def git_commit(message: str):
    """Commit staged changes with a message."""
    # Escape quotes in commit message
    escaped_message = message.replace('"', '\\"')
    success, stdout, stderr = _run_git_command(f'git commit -m "{escaped_message}"')
    
    if success:
        return f"✅ Committed changes: {message}"
    else:
        return f"❌ Git commit failed: {stderr}"

@register_command("git push", safe=False)
def git_push():
    """Push commits to remote repository."""
    success, stdout, stderr = _run_git_command("git push")
    
    if success:
        return "✅ Successfully pushed to remote repository"
    else:
        return f"❌ Git push failed: {stderr}"

@register_command("git pull", safe=False)
def git_pull():
    """Pull latest changes from remote repository."""
    success, stdout, stderr = _run_git_command("git pull")
    
    if success:
        if "Already up to date" in stdout:
            return "✅ Repository is already up to date"
        else:
            return f"✅ Pulled changes: {stdout}"
    else:
        return f"❌ Git pull failed: {stderr}"

@register_command("create new branch {name}", safe=False)
def create_branch(name: str):
    """Create and switch to a new git branch."""
    success, stdout, stderr = _run_git_command(f"git checkout -b {name}")
    
    if success:
        return f"✅ Created and switched to new branch: {name}"
    else:
        return f"❌ Failed to create branch: {stderr}"

@register_command("switch to branch {name}", safe=False)
def switch_branch(name: str):
    """Switch to an existing git branch."""
    success, stdout, stderr = _run_git_command(f"git checkout {name}")
    
    if success:
        return f"✅ Switched to branch: {name}"
    else:
        return f"❌ Failed to switch branch: {stderr}"

@register_command("list git branches", safe=True)
def list_branches():
    """List all git branches."""
    success, stdout, stderr = _run_git_command("git branch")
    
    if not success:
        return f"❌ Git error: {stderr}"
    
    if not stdout:
        return "❌ No branches found"
    
    branches = []
    current_branch = None
    
    for line in stdout.split('\n'):
        line = line.strip()
        if line.startswith('* '):
            current_branch = line[2:]
            branches.append(f"* {current_branch} (current)")
        elif line:
            branches.append(f"  {line}")
    
    return f"🌿 Git branches:\n" + "\n".join(branches)

@register_command("get current branch", safe=True)
def get_current_branch():
    """Get the name of the current git branch."""
    success, stdout, stderr = _run_git_command("git branch --show-current")
    
    if success and stdout:
        return f"🌿 Current branch: {stdout}"
    else:
        return f"❌ Could not determine current branch: {stderr}"

@register_command("git log last {count} commits", safe=True)
def git_log(count: int = 5):
    """Show the last N commit messages."""
    if count > 20:
        count = 20  # Limit to prevent spam
    
    success, stdout, stderr = _run_git_command(f"git log --oneline -n {count}")
    
    if not success:
        return f"❌ Git log failed: {stderr}"
    
    if not stdout:
        return "❌ No commits found"
    
    return f"📜 Last {count} commits:\n{stdout}"

@register_command("check git remote", safe=True)
def check_remote():
    """Check git remote repository information."""
    success, stdout, stderr = _run_git_command("git remote -v")
    
    if not success:
        return f"❌ Git error: {stderr}"
    
    if not stdout:
        return "📡 No remote repositories configured"
    
    return f"📡 Remote repositories:\n{stdout}"
