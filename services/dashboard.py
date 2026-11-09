import streamlit as st
from common.config import AppConfig
import pandas as pd

def render():
    # Odczyt danych
    FILE = AppConfig.FILENAME
    df = pd.read_csv(FILE)
    # Ustawienia aplikacji
    st.set_page_config(
        page_title="Aplikacja pogodowa",
        layout="wide",
    )
    # Utwórz element title ze streamlita
    st.title("Aplikacja pogodowa")
    st.subheader("Dane pogodowe dla wybranych miast")
    # Pasek boczny z ustawieniami
    st.sidebar.header("Konfiguracja")
    # Wybór ilości wierszy w tabelce
    # Cyfra mówiąca o ilości wierszy
    selected_rows = st.sidebar.slider(
        "Ilość rekordów w tabeli",
        min_value=1,
        max_value=100,
        value=10, # domyślna wartość
    )
    # Wybór kolumny w wykresie
    selected_col = st.sidebar.selectbox(
        "Wybierz nazwę kolumny",
        ["temp","feels_like","wind"]
    )
    st.divider()
    # Aktualna / najnowsza pogoda
    st.subheader("Aktualna pogoda")
    # Informacje o najnowszym rekordzie pogodowym
    last_row = df.iloc[-1]
    cols = st.columns(4)
    with cols[0]:
        temp = last_row.get("temp")
        cols[0].metric("Temperatura", temp)
    with cols[1]:
        feels_like = last_row.get("feels_like")
        cols[1].metric("Odczuwalna", feels_like)
    with cols[2]:
        wind = last_row.get("wind")
        cols[2].metric("Prędkość wiatru", wind)
    with cols[3]:
        sunrise = last_row.get("sunrise")
        cols[3].metric("Wschód słońca", sunrise)

    st.divider()
    # Tabela z wynikami
    st.subheader("Tabela z wynikami")
    rows = df.head(int(selected_rows))
    st.dataframe(rows)

    st.divider()

    # Wykresy liniowe
    st.subheader("Temperatura w czasie")
    temp_chart = df.set_index(
        "timestamp"
    )[["temp","feels_like"]]
    st.line_chart(temp_chart)
    # Wykres z wyborem kolumny
    st.subheader("Customowy wykres")
    custom_chart = df.set_index(
        "timestamp"
    )[[selected_col]]
    st.line_chart(custom_chart)