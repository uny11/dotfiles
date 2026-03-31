#!/bin/sh

# systray volume
volumeicon &

#unidades externas
udiskie -t &

#bloqueo de pantalla en 10min
xautolock -time 10 -locker "betterlockscreen -l" &
