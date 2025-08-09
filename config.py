from pathlib import Path

class Config:
    off_state = [
        "\nactive-opacity = 1",
        "\ninactive-opacity = 1",
    ]
    on_state = [
        "\nactive-opacity = 0.925",
        "\ninactive-opacity = 0.925",
    ]
    file_target = Path.home() / ".config" / "picom" / "picom.conf"
