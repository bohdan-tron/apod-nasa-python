import streamlit as st
import requests as req
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='envs/.env')


api_key = os.environ.get('NASA_API_KEY')
image_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
r = req.get(image_url)
data = r.json()


st.title("Space pic of the day")
st.header(data['title'])
st.image(data['url'])
st.write(data['copyright'])
st.write(data['explanation'])

