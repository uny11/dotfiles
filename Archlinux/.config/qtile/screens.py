
from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.92)


screens = [Screen(top=status_bar(primary_widgets))]

#xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
xrandr = 'xrandr --output HDMI-0 --off --output DP-0 --mode 1920x1200 --pos 0x0 --rotate left --output DP-1 --off --output DP-2 --primary --mode 1920x1080 --pos 1200x376 --rotate normal --output DP-3 --off --output DP-4 --off --output DP-5 --off'

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))