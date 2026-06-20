"""Lumina's shared visual language and filesystem-safe asset helpers."""

from pathlib import Path

APP_NAME = "Lumina"
TAGLINE = "Hikâyeler burada ışık bulur."
ASSET_DIR = Path(__file__).resolve().parent.parent / "assets"
ICON_DIR = ASSET_DIR / "icons"

# Aurora palette: accessible contrast in both appearance modes.
BACKGROUND = ("#F5F7FC", "#080D1A")
PANEL = ("#FFFFFF", "#11192B")
PANEL_ELEVATED = ("#EEF2FF", "#18233A")
PRIMARY = ("#6857E5", "#8B7CFF")
PRIMARY_HOVER = ("#5545C7", "#7565EA")
SUCCESS = ("#168B75", "#2DD4BF")
DANGER = ("#D1435B", "#FB7185")
WARNING = ("#B86E00", "#FBBF24")
TEXT = ("#172033", "#F7F8FC")
TEXT_MUTED = ("#687086", "#9AA6BD")
BORDER = ("#DDE3F0", "#263552")
SIDEBAR = ("#EEF2FF", "#0D1424")

FONT_FAMILY = "Segoe UI"


def icon_path(filename: str) -> Path:
    return ICON_DIR / filename
