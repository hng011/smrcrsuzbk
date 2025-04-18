import streamlit as st
import requests
from dotenv import load_dotenv
import os
import json
import time


load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or st.secrets("OPENROUTER_API_KEY")
G_API_KEY = os.getenv("G_API_KEY") or st.secrets("G_API_KEY")

G_API_ENDPOINT = os.getenv("G_API_ENDPOINT") or st.secrets("G_API_ENDPOINT")
OPENROUTER_ENDPOINT = os.getenv("OPENROUTER_ENDPOINT") or st.secrets("OPENROUTER_ENDPOINT")
