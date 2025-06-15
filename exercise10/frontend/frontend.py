import streamlit as st
import requests
from urllib.parse import urlparse, parse_qs

st.set_page_config(page_title="Weather App", layout="centered")

query_params = st.query_params
city = query_params.get("city", [])

if city:
    st.title(f"Weather Forecast for {city}")

    try:
        backend_url = f"https://weather-forecast-backend-3wba.onrender.com/weather?city={city}"
        response = requests.get(backend_url)

        if response.status_code == 200:
            data = response.json()

            st.write(f"**Location:** {data['location']['name']}, {data['location']['country']}")
            st.write(f"**Current Temperature:** {data['current']['temp_c']}°C")
            st.write("---")

            for day in data["forecast"]["forecastday"]:
                st.markdown(f"### {day['date']}")
                st.write(f"Max Temp: {day['day']['maxtemp_c']}°C")
                st.write(f"Min Temp: {day['day']['mintemp_c']}°C")
                st.markdown(f"Condition: {day['day']['condition']['text']} ![icon](https:{day['day']['condition']['icon']})")

        else:
            st.error("Failed to fetch weather data.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please specify a city in the URL. Example: `/?city=Cracow`")

