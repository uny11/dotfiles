
import requests
import time,datetime
from dotenv import load_dotenv
import os
import csv


# Cargar API Key desde .env
load_dotenv()
API_KEY = os.getenv("METEOCAT_API_KEY")

print (API_KEY)