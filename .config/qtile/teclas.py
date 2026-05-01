
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

mod = "mod4"

terminal = guess_terminal()

keys = [

    # FOCUS
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "period", lazy.next_screen(), desc="Siguiente monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Anterior monitor"),

    # Mover ventana al monitor izquierdo o derecho (Win + Shift + ←)
    Key(["mod4", "shift"], "Left", lazy.to_screen(-1)),
    Key(["mod4", "shift"], "Right", lazy.to_screen(1)),

    # Esto envía la ventana activa al grupo (espacio) indicado
    Key(["mod4", "shift"], "1", lazy.window.togroup("1")),
    Key(["mod4", "shift"], "2", lazy.window.togroup("2")),
    Key(["mod4", "shift"], "3", lazy.window.togroup("3")),
    Key(["mod4", "shift"], "4", lazy.window.togroup("4")),
    Key(["mod4", "shift"], "5", lazy.window.togroup("5")),
    Key(["mod4", "shift"], "6", lazy.window.togroup("6")),

    #Apps
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "c", lazy.spawn("code --ozone-platform=x11")),
    Key([mod], "b", lazy.spawn("brave")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    #Bloqueo de pantalla
    Key([mod, "control"], "b", lazy.spawn("betterlockscreen -l"), desc="Bloquear Pantalla"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )
