import pandas as pd
import os
from common.config import AppConfig
# Import był nam potrzebny tylko do instalacji
# import openpyxl

FILE = AppConfig.FILENAME

# Z danych, które dotarły do mnie w parametrze dataset
# utwórz obiekt DataFrame (pochodzący z Pandas)
def save_to_excel(dataset):
    try:
        # Nowe dane wrzucamy do df
        new_df = pd.DataFrame(dataset)
        # Sprawdź czy ścieżka istnieje
        if os.path.exists(FILE):
            # Stare dane odczytujemy - read_ tworzy df
            old_df = pd.read_excel(FILE)
            # Finalny df składający się z nowych i starych elementów
            df = pd.concat([old_df, new_df], ignore_index=True)
        else:
            df = new_df

        # DF w zależności którą ścieżką podążył program będzie tylko nowym
        # albo nowym i starym
        df.to_excel(FILE, index=False)

        print("Dane zostały zapisane w pliku")

    except Exception as e:
        print(e)


def read_excel():
    df = pd.read_excel(FILE)
    return df