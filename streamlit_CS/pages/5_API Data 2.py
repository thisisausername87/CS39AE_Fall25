#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(page_title="Live API Demo (Open-Meteo)", page_icon="🌤️", layout="wide")

# Disable fade/transition so charts don't blink between reruns
st.markdown("""
    <style>
      [data-testid="stPlotlyChart"], .stPlotlyChart, .stElementContainer {
        transition: none !important;
        opacity: 1 !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("🌤️ Live Weather Data Demo (Open-Meteo)")
st.caption("Displays current and recent weather conditions using the Open-Meteo API.")

# --------------------------------------------------
#  API SETUP
# --------------------------------------------------
lat, lon = 39.7392, -104.9903  # Denver, CO
wurl = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,wind_speed_10m&timezone=auto"

@st.cache_data(ttl=600, show_spinner=False)  # cache for 10 minutes
def get_weather():
    """Fetch hourly weather data and return DataFrame."""
    try:
        r = requests.get(wurl, timeout=10)
        r.raise_for_status()
        j = r.json()["hourly"]
        df = pd.DataFrame({
            "Time": pd.to_datetime(j["time"]),
            "Temperature (°C)": j["temperature_2m"],
            "Wind Speed (m/s)": j["wind_speed_10m"]
        })
        return df, None
    except requests.RequestException as e:
        return None, f"Network/HTTP error: {e}"

# --------------------------------------------------
#  AUTO REFRESH CONTROLS
# --------------------------------------------------
st.subheader("🔁 Auto Refresh Settings")

refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)

st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

# --------------------------------------------------
#  WEATHER DATA
# --------------------------------------------------
st.subheader("Weather Data (Hourly Forecast)")

df, err = get_weather()

if err:
    st.warning(f"{err}\nUsing fallback data.")
    df = pd.DataFrame({
        "time": pd.date_range(end=pd.Timestamp.now(), periods=5, freq="H"),
        "temperature (°C)": [10, 11, 12, 13, 14],
        "wind speed (m/s)": [2, 3, 2.5, 3.2, 2.8]
    })

st.dataframe(df.tail(10), use_container_width=True)

# --------------------------------------------------
#  LINE CHART
# --------------------------------------------------
fig = px.line(
    df,
    x="time",
    y=["temperature (°C)", "wind speed (m/s)"],
    title="Hourly Weather Forecast (Temperature & Wind Speed)",
    labels={"value": "Measurement", "time": "Time"},
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
#  AUTO REFRESH LOOP
# --------------------------------------------------
if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    st.rerun()

