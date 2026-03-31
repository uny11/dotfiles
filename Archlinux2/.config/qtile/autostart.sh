#!/bin/sh

# Iniciar ssh-agent para entorno gráfico
if [ -z "$SSH_AUTH_SOCK" ]; then
    eval "$(ssh-agent -s)" > /dev/null
    ssh-add ~/.ssh/id_ed25519 2> /dev/null
fi

# systray volume
volumeicon &

#unidades externas
udiskie -t &

#bloqueo de pantalla en 10min
xautolock -time 10 -locker "betterlockscreen -l" &
