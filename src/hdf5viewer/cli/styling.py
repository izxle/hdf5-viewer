"""Wrap string in color code characters."""


def color(string: str, cli_color: str) -> str:
    """Wrap string in color code characters."""
    match cli_color:
        case "normal":
            color_code = "\x1b[0m"
        case "black":
            color_code = "\x1b[30m"
        case "red":
            color_code = "\x1b[31m"
        case "green":
            color_code = "\x1b[32m"
        case "yellow":
            color_code = "\x1b[33m"
        case "blue":
            color_code = "\x1b[34m"
        case "magenta":
            color_code = "\x1b[35m"
        case "cyan":
            color_code = "\x1b[36m"
        case "white":
            color_code = "\x1b[37m"
        case "bright black":
            color_code = "\x1b[90m"
        case "bright red":
            color_code = "\x1b[91m"
        case "bright green":
            color_code = "\x1b[92m"
        case "bright yellow":
            color_code = "\x1b[93m"
        case "bright blue":
            color_code = "\x1b[94m"
        case "bright magenta":
            color_code = "\x1b[95m"
        case "bright cyan":
            color_code = "\x1b[96m"
        case "bright white":
            color_code = "\x1b[97m"
        case _:
            color_code = "\x1b[0m"

    return f"{color_code}{string}\x1b[0m"
