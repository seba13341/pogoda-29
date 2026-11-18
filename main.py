# Ze ścieżki services/openweather importuj element get_weather
from services.openweather import get_weather
from services.files import save_to_excel
from services.dashboard import render
from services.mysql_db import create_weather_table, insert_weather
import time

# render()
create_weather_table()

while True:
    # Pod zmienną weather kryją się pobrane - aktualne dane pogodowe
    weather = get_weather()
    save_to_excel([weather])

    insert_weather(weather)

    # Po każdej iteracji śpij na X czasu
    # zapobiegnie to nieskończonej pętli - tysiące razy na sekundę
    time.sleep(15)