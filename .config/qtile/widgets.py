
from libqtile import widget
from theme import colors

widget_defaults = dict(
    font="Adwaita",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()


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
        #text="󰄽", # Icon: nf-md-chevron_double_left
        text="", # Icon: nf-md-menu_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.CurrentLayout(**base(bg='color2'), scale=0.65, mode='icon'),
        widget.CurrentLayout(**base(bg='color2'), padding=5),
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Monofur',
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
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),        
    ]




primary_widgets = [

    *workspaces(),

    separator(),

    # powerline('color1', 'dark'),

    # icon(bg="color1", text=' '), # Icon: nf-fa-volume_high

    # widget.Volume(
    #     foreground=colors['dark'],
    #     background=colors['color1'],
    #     channel='Headphone',
    # ),

    # powerline('color4', 'color1'),

    # icon(bg="color4", text=' '), # Icon: nf-fa-volume_high

    # widget.Volume(
    #     foreground=colors['dark'],
    #     background=colors['color4'],
    #     channel='Master',
    # ),

    # powerline('color3', 'dark'),
   
    # icon(bg="color3", text='󰿅 '), # Icon: nf-md-location_exit
    
    # widget.QuickExit(
    #     foreground=colors['dark'],
    #     background=colors['color3'],
    #     default_text='EXIT',
    # ),
    

    #powerline('color3', 'color3'),
]


secondary_widgets = [

    *workspaces(),

    separator(),

    widget.Systray(background=colors['dark'], padding=5),

    powerline('color1', 'dark'),

    icon(bg="color1", text=' '), # Icon: nf-fa-volume_high

    widget.Volume(
        foreground=colors['dark'],
        background=colors['color1'],
        channel='Headphone',
    ),

    powerline('color4', 'color1'),

    icon(bg="color4", text=' '), # Icon: nf-fa-volume_high

    widget.Volume(
        foreground=colors['dark'],
        background=colors['color4'],
        channel='Master',
    ),
    
    powerline('color3', 'color4'),

    # icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    # widget.Net(
    #     **base(bg='color3'), 
    #     interface='wlan0',
    #     format='{down:6.2f}{down_suffix:<2}↓↑{up:6.2f}{up_suffix:<2}'
    # ),
 
    icon(bg="color3", text='󰍛 '),  # Icon: nf-md-memory

    widget.Memory(
        foreground=colors['dark'],
        background=colors['color3'],
        measure_mem='G',       
    ),

    powerline('color1', 'color3'),

    icon(bg="color1", text=' '), # Icon: nf-fa-hdd_o

    widget.HDD(
        foreground=colors['dark'],
        background=colors['color1'],
        format='{HDDPercent}%',
        device='nvme0n1',
    ),

    powerline('color4', 'color1'),

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

    powerline('color1', 'color3'),

    icon(bg="color1", text=' '), # Icon: nf-md-calendar

    widget.Clock(
        **base(fg='dark',bg='color1'), 
        #format='%d/%m/%Y - %H:%M'
        format='%d/%m - %H:%M'
    ),

    powerline('color4', 'color1'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        foreground=colors['dark'],
        background=colors['color4'],
        colour_have_updates=colors['dark'],
        colour_no_updates=colors['dark'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),
   
    icon(bg="color3", text='󰿅 '), # Icon: nf-md-location_exit
    
    widget.QuickExit(
        foreground=colors['dark'],
        background=colors['color3'],
        default_text='EXIT',
    ),
    
     
]