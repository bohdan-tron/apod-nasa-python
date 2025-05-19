import streamlit as st
import requests as req
import os
from datetime import date
from dotenv import load_dotenv
from config import NASA_API_ENDPOINT, ENV_FILE_PATH
from typing import Optional, Dict, Any


load_dotenv(dotenv_path=ENV_FILE_PATH)
api_key = os.environ.get('NASA_API_KEY')
api_query = f"{NASA_API_ENDPOINT}?api_key={api_key}"

today = date.today()
selected_date = st.date_input(
  "Select date",
  value=today
)

if selected_date > today:
  st.error("Please select a date no later than today")
  st.stop()

api_query = f"{NASA_API_ENDPOINT}?api_key={api_key}&date={selected_date}"


@st.cache_resource
def get_nasa_image(url_to_load) -> Optional[Dict[str, Any]]:
  r = req.get(url_to_load, timeout=10)
  data = r.json()
  return data


with st.spinner('Fetching data from NASA API...'):
  st.cache_resource.clear()
  data: Dict[str, Any] | None = get_nasa_image(api_query)


st.title("Space pic of the day")

if data is None:
  st.write("Error getting data from NASA API")
  exit()

st.header(data['title'])

try:
  st.image(data['url'])
except:
  st.write("No image found")

try:
  st.write(data['copyright'])
except:
  st.write("No copyright found")

try:
  st.write(data['explanation'])
except:
  st.write("No explanation found")
