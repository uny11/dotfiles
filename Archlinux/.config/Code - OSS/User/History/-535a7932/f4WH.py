# Qtile Config File
# http://www.qtile.org/

# Isaac Porta
# 01-Junio-2025
# https://github.com/uny11/dotfiles
# basado en: https://github.com/antoniosarosi/dotfiles de Antonio Sarosi

from libqtile import hook

from teclas import mod, keys
from groups import groups
from layouts import layouts, floating_layout
from widgets import widget_defaults, extension_defaults
#from settings.screens import screens
from mouse import mouse
from path import qtile_path

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'

