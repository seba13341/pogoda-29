from services.openweather import get_weather
from services.files import save_to_excel


from services.dashboard import render

import time


render()
#while True:
#    try:
        # Pod zmienną weather kryją się pobrane - aktualne dane pogodowe
#        weather = get_weather()
#        save_to_excel([weather])
#        print("Pobrano i zapisano dane pogodowe.")
#    except Exception as e:
 #       print(f"Wystąpił błąd: {e}")

#    time.sleep(15)