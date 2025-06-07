
import requests
import schedule
import time
from dotenv import load_dotenv
import os

# Cargar API Key desde .env
load_dotenv()
API_KEY = os.getenv("METEOCAT_API_KEY")
COD_ESTACIO = "UG"  # Ejemplo: Barcelona (consulta los códigos en la documentación)

def obtener_datos_meteocat():
    url = f"https://api.meteocat.gencat.cat/v1/meteo/observacio/estacions/{COD_ESTACIO}/ultimes/24h"
    
    headers = {
        "x-api-key": API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        datos = response.json()
        
        if response.status_code == 200:
            print("\n🌦️ Datos meteorológicos (Meteocat):")
            for medicion in datos:
                variable = medicion["variable"]["nom"]
                valor = medicion["valor"]
                data = medicion["data"]
                print(f"📅 {data} | {variable}: {valor}")
        else:
            print(f"❌ Error {response.status_code}: {datos.get('message', 'Sin detalles')}")
    
    except Exception as e:
        print(f"🚨 Error: {e}")

# Configurar periodicidad (ej: cada 30 minutos)
schedule.every(30).minutes.do(obtener_datos_meteocat)

# Primera ejecución
obtener_datos_meteocat()

# Bucle infinito
while True:
    schedule.run_pending()
    time.sleep(1)