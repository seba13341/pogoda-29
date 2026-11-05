import pandas as pd
import os
from common.config import AppConfig


FILE = AppConfig.FILENAME

def save_to_excel(dataset):
    try:
        new_df = pd.DataFrame(dataset)
        if os.path.exists(FILE):
            old_df = pd.read_excel(FILE)
            df = pd.concat([old_df, new_df], ignore_index=True)
        else:
            df = new_df

        df.to_excel(FILE, index=False)

        print("Dane zostały zapisane w pliku")

    except Exception as e:
        print(e)


def read_excel():
    df = pd.read_excel(FILE)
    return df
