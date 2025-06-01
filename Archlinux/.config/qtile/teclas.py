# Isaac Porta
# 01-Junio-2025
# https://github.com/uny11/dotfiles

# Atajos de teclado

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

terminal = guess_terminal()

mod = "mod4"


keys = [

    # Ventanas
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "period", lazy.next_screen(), desc="siguiente monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="anterior monitor"),

    #qtile
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    #Apps
    Key([mod], "m", lazy.spawn("rofi -show run"), desc="Launch rofi"),
    Key([mod], "f", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch code"),
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master unmute")),
    
    ]