# src/app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Cargar el modelo al iniciar la app
model = joblib.load('models/model.pkl')

# 2. Definir la estructura de los datos de entrada (las medidas de la flor)
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 3. Iniciar la app
app = FastAPI(title="Iris ML API")

@app.get("/")
def home():
    return {"message": "MLOps API funcionando!"}

@app.post("/predict")
def predict(data: IrisInput):
    # Convertir los datos recibidos a un array de numpy
    features = np.array([[
        data.sepal_length, 
        data.sepal_width, 
        data.petal_length, 
        data.petal_width
    ]])
    
    # Hacer la predicción
    prediction = model.predict(features)
    
    # Devolver el resultado (convertimos a int para que sea JSON serializable)
    return {"class": int(prediction[0])}
