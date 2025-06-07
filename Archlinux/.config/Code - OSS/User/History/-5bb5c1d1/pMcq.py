# Isaac Porta
# 01-Junio-2025
# https://github.com/uny11/dotfiles

from libqtile import widget
from theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),
        widget.CurrentLayout(**base(bg='color2'), padding=5),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),        
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(
        **base(bg='color3'), 
        interface='wlo1',
        format='{down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}'
    ),

    powerline('color3', 'color1'),

    icon(bg="color1", text=''), # Icon: nf-md-calendar

    widget.Clock(
        **base(bg='color1'), 
        format='%d/%m/%y - %H:%M'
    ),

    powerline('color1', 'color2'),

    icon(bg="color2", text=' '), # Icon: nf-fa-volume_high

    widget.Volume(
        foreground=colors['dark'],
        background=colors['color2'],
        channel='Headset',
    ),

    powerline('color1', 'color4'),

    icon(bg="color4", text='󰈸 '), # Icon: nf-md-fire

    widget.NvidiaSensors(
        foreground=colors['dark'],
        background=colors['color4'],
        threshold=60, 
        foreground_alert='ff6000',
    ),

    powerline('color3', 'color4'),

    icon(bg="color3", text='󰻠 '),  # Icon: nf-fmd-cpu_64_bit
    
    widget.CPU(
        foreground=colors['dark'],
        background=colors['color3'],
        format='{load_percent}%',
    ),

    powerline('color3', 'color1'),

    icon(bg="color1", text=' '), # Icon: nf-fa-hdd_o

    widget.HDD(
        foreground=colors['dark'],
        background=colors['color1'],
        format='{HDDPercent}%',
        device='nvme0n1',
    ),

    powerline('color1', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

    powerline('dark', 'color2'),

    icon(bg="color2", text='󰿅  '), # Icon: nf-md-location_exit
    
    widget.QuickExit(
        foreground=colors['dark'],
        background=colors['color2'],
        default_text='Salir',
    ),
    
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()