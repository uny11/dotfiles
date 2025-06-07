import requests  # Para hacer peticiones HTTP a la API
import logging  # Para registrar eventos en un archivo de log
import os  
from datetime import datetime 
from dotenv import load_dotenv

# Cargar API Key desde .env
load_dotenv()

#Pedir variable de dia
DIA = input("De quin dia vols recollir les dades? (Exemple: 2025/06/03) : ")
ESTACIO = input("De quina estacio? (Exemple: WP - Canaletes) : ")

URL = "https://api.meteo.cat/xema/v1/estacions/mesurades/" + ESTACIO + "/" + DIA

print (URL)