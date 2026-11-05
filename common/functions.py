def k_to_celsius(temp):
    # Działanie z temperaturą zaokrąglij do 2 miejsc po przecinku i zwróć
    return round(temp - 273.15, 2)


def ms_to_kmh(speed):
    # Zamień m/s na km/h (mnożąc przez 3.6) i zaokrąglij do 2 miejsc po przecinku
    return round(speed * 3.6, 2)