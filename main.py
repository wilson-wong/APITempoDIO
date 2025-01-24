from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à APITempoDIO!"}

@app.get("/tempo")
def obter_tempo():
    return {"cidade": "São Paulo", "temperatura": "25°C", "condição": "Ensolarado"}