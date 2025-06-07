
import requests  # Para hacer peticiones HTTP a la API
import logging  # Para registrar eventos en un archivo de log
import os  
from datetime import datetime 
from dotenv import load_dotenv

# Cargar API Key desde .env
load_dotenv()

# Configuración (variables que puedes modificar)
DATABASE_URL = 'https://api.meteo.cat/xema/v1/representatives/metadades/municipis/082401/variables/32' # URL de la API
#DATABASE_URL = 'https://api.meteo.cat/xema/v1/estacions/DI/metadades'
API_KEY = os.getenv('METEOCAT_API_KEY')  # Clave API (mejor desde variable de entorno)
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'data')  # Carpeta para guardar datos
LOG_FILE = os.path.join(os.path.dirname(__file__), 'logs', 'Temps.log')  # Archivo de log

def setup_logging():
    # Crea los directorios si no existen
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Configura el sistema de logging
    logging.basicConfig(
        filename=LOG_FILE,  # Archivo donde se guardan los logs
        level=logging.INFO,  # Nivel de detalle (INFO, WARNING, ERROR)
        format='%(asctime)s - %(levelname)s - %(message)s'  # Formato del log
    )

def download_data():
    try:
        # Escribe en el log que comenzó la descarga
        logging.info("Iniciando descarga de datos")
        
        # Prepara los headers y parámetros para la petición HTTP
        headers={"Content-Type": "application/json", "X-Api-Key": API_KEY}
        #params = {'limit': 1000}  # Límite de registros a descargar
        
        # Hace la petición GET a la API
        response = requests.get(DATABASE_URL, headers=headers) #, params=params)
        response.raise_for_status()  # Lanza error si la petición falló
        
        # Genera un nombre de archivo con la fecha/hora actual
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(OUTPUT_DIR, f"data_{timestamp}.json")
        
        # Guarda los datos en un archivo JSON
        with open(output_file, 'w') as f:
            f.write(response.text)
            
        # Registra éxito en el log
        logging.info(f"Datos descargados correctamente en {output_file}")
        return True
        
    except requests.exceptions.RequestException as e:
        # Captura errores de conexión/HTTP
        logging.error(f"Error de conexión: {str(e)}")
    except Exception as e:
        # Captura cualquier otro error inesperado
        logging.error(f"Error inesperado: {str(e)}")
    return False

if __name__ == "__main__":
    # Punto de entrada del script
    setup_logging()  # Configura el sistema de logs
    download_data()  # Ejecuta la descarga
