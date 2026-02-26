from pathlib import *

from rich.console import Console
from rich.theme import Theme
from colorama import *


IMAGE_PATH = Path(__file__).absolute().parent / "Images" / "ascii_image.txt"


myStyle:dict = {
    "success": "bold green",
    "error": "bold underline red",
    "important":"bold underline blue",
    "info": "bold cyan"
} 

terminal_theme = Theme(myStyle)

terminal = Console(theme=terminal_theme)
