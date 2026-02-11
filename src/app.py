# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# 1. Cargar el modelo
model_path = 'models/model.pkl'

if not os.path.exists(model_path):
    # En producción (Docker), a veces las rutas cambian, esto ayuda a depurar
    model_path = 'model.pkl' 

if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None # Manejo de error suave

# 2. Definir datos de entrada
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 3. Crear APP
app = FastAPI(title="Iris ML API")

@app.get("/")
def home():
    return {"message": "API de MLOps funcionando correctamente"}

@app.post("/predict")
def predict(data: IrisInput):
    if not model:
        return {"error": "Modelo no encontrado"}
        
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])
    prediction = model.predict(features)
    return {"class": int(prediction[0])}
