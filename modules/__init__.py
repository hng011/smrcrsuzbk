import streamlit as st
import requests
import dotenv
import os
import json
import time


dotenv.load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY") or st.secrets("OPENROUTER_API_KEY")
OPENROUTER_ENDPOINT = os.getenv("OPENROUTER_ENDPOINT") or st.secrets("OPENROUTER_ENDPOINT")