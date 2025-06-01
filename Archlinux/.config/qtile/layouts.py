# Isaac Porta
# 01-Junio-2025
# https://github.com/uny11/dotfiles

# Layouts

from libqtile import layout
from libqtile.config import Match
from theme import colors

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.TreeTab(),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    layout.Max(),
    layout.Columns(),
    layout.Tile(),
    layout.VerticalTile(),
    layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)