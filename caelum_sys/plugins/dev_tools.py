from caelum_sys.registry import register_command


@register_command("open vs code")
def open_vs_code():
    import subprocess

    try:
        subprocess.Popen("code")  # Assumes VS Code is in PATH
        return "🧑‍💻 VS Code opened."
    except Exception as e:
        return f"❌ Failed to open VS Code: {e}"


@register_command("list installed packages")
def list_installed_packages():
    import pkg_resources

    packages = sorted([p.project_name for p in pkg_resources.working_set])
    return "📦 Installed packages:\n" + "\n".join(f"- {p}" for p in packages)
