
#!/bin/bash

# Verificar que se proporcionen los argumentos necesarios
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <carpeta_origen> <carpeta_destino>"
    exit 1
fi

origen="$1"
destino="$2"

# Verificar que las carpetas existan
if [ ! -d "$origen" ]; then
    echo "Error: La carpeta de origen '$origen' no existe."
    exit 1
fi

if [ ! -d "$destino" ]; then
    echo "Error: La carpeta de destino '$destino' no existe."
    exit 1
fi

# Usar rsync para copiar solo archivos nuevos o modificados
rsync -avu --progress "$origen/" "$destino/"

echo "Copia completada. Solo se han copiado archivos nuevos o modificados."
    