
import requests
import time,datetime
#import schedule
from dotenv import load_dotenv
import os
import csv


# Cargar API Key desde .env
load_dotenv()
API_KEY = os.getenv("METEOCAT_API_KEY")
url = 'https://api.meteo.cat/referencia/v1/municipis'
 
response = requests.get(url, headers={"Content-Type": "application/json", "X-Api-Key": API_KEY})
 
print(response.status_code)  #statusCode
print(response.text) #valors de la resposta



