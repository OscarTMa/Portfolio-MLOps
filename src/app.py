# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# 1. Cargar el modelo (buscamos la ruta correcta)
model_path = 'models/model.pkl'

if not os.path.exists(model_path):
    raise FileNotFoundError(f"No se encontró el modelo en {model_path}. Ejecuta train.py primero.")

model = joblib.load(model_path)

# 2. Definir qué datos esperamos recibir (Validación de datos)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 3. Crear la APP
app = FastAPI(title="Mi Primera API de MLOps")

@app.get("/")
def home():
    return {"mensaje": "¡La API está viva! Usa /docs para probarla."}

@app.post("/predict")
def predict(data: IrisInput):
    # Convertimos los datos que llegan en un formato que el modelo entienda
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])
    
    # Hacemos la predicción
    prediction = model.predict(features)
    
    # El modelo devuelve un número (0, 1, 2), lo convertimos a int simple
    return {"clase_predicha": int(prediction[0])}
