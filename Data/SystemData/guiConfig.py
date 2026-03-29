from pathlib import *
from customtkinter import FontManager

FONT_PATH = Path(__file__).absolute().parent / "VCR_OSD_MONO_1.001.ttf"


FontManager.load_font(str(FONT_PATH))

smileFont = ("VCR OSD Mono",20)


colors = {
    "dark_grey": "#2e2e2e",
    "darker_grey": "#252525",
    "darkest_grey": "#181818",
    
    "window_bg":        "#1e1e1e",
    "titlebar_top":     "#8b1a1a",
    "titlebar_bot":     "#6b1111",
    "titlebar_border":  "#3a0808",
    "left_panel":       "#252525",
    "right_panel":      "#2a2a2a",
    "panel_border":     "#5a1a1a",
    "tip_header_top":   "#7a1111",
    "tip_header_bot":   "#5e0d0d",
    "tip_body":         "#1c1c1c",
    "tip_text":         "#c0c0c0",
    "tip_highlight":    "#4ecc85",
    "btn_bg":           "#2e2e2e",
    "btn_border":       "#404040",
    "btn_text":         "#dddddd",
    "btn_hover":        "#3a3a3a",
    "btn_active_bg":    "#3d1010",
    "btn_active_border":"#8b1a1a",
    "btn_active_text":  "#f0c0c0",
    "logo_white":       "#f5f5f5",
    "logo_red":         "#e05050",
    "title_text":       "#f0d0d0",
    "status_bar":       "#1a1a1a",
    "status_dot":       "#4ecc85",
    "status_text":      "#888888",
    "wc_min":           "#888888",
    "wc_max":           "#555555",
    "wc_close":         "#c0392b",
}

