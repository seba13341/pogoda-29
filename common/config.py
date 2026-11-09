from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
    # Serwer - wartość dla zmiennej API_KEY weź z pliku .env ze zmiennej API_KEY
    API_KEY = os.getenv("API_KEY")
    CITY = "Lisbon"
    FILENAME = "pogoda_2026.csv"