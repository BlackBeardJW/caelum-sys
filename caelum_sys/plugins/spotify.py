from caelum_sys.registry import register_command

@register_command("play spotify")
def play_spotify(command: str):
    # Extract query after command trigger
    query = command[len("play spotify"):].strip()
    if query:
        return f"🎵 Pretending to play: '{query}' on Spotify."
    return "🎵 Opening Spotify (simulated)."
