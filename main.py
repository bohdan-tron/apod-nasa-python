import streamlit as st
import requests as req
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='envs/.env')


@st.cache_resource
def get_nasa_image():
  print('its uncached')
  api_key = os.environ.get('NASA_API_KEY')
  image_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
  r = req.get(image_url)
  data = r.json()
  return data


data = get_nasa_image()


st.title("Space pic of the day")

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

