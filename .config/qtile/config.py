
from libqtile import hook
import os
import libqtile.resources

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from pantallas import screens
from teclas import mod, keys
from widgets import widget_defaults, extension_defaults


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Define los nombres de tus grupos
nombres_grupos = ["   ", " 󰨞  ", "   ", " 󰊢  ", "  ", "  "]

# Crea los grupos con screen_affinity para asignar pantallas
groups = []
for i, nombre in enumerate(nombres_grupos):
    if i == 0: 
        groups.append(Group(nombre, screen_affinity=1))
    elif i == 1: 
        groups.append(Group(nombre, screen_affinity=1))
    elif i == 2: 
        groups.append(Group(nombre, screen_affinity=1))
    elif i == 3: 
        groups.append(Group(nombre, screen_affinity=1))
    elif i == 4: 
        groups.append(Group(nombre, screen_affinity=1))
    elif i == 5: 
        groups.append(Group(nombre, screen_affinity=0))
    else:
        groups.append(Group(nombre))

# groups = [Group(i) for i in [
#     "   ", " 󰨞  ", "   ", " 󰊢  ", "  ", "  "
# ]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
    qtile.to_screen(1)  #cambiar focus de pantalla 2


layouts = [
    layout.MonadTall(),    
    layout.MonadWide(),
    layout.Max(),
    layout.TreeTab(),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.RatioTile(),
    #layout.Tile(),
    layout.VerticalTile(),
    #layout.Floating(),
    #layout.Zoomy(),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



main = None
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "urgent"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

idle_inhibitors = []  # type: list

wmname = "Qtile"



