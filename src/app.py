from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import pandas as pd
import logging
from fastapi.responses import FileResponse
from .config import DATA_PATH, FORECAST_HORIZON, target
from .data_preprocessing import load_and_preprocess_data
from .model_predict import predict_with_var

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Crear la app
app = FastAPI(title="VAR Power Consumption API", version="1.0")

# Modelo de entrada opcional (POST con datos manuales)
class DataInput(BaseModel):
    values: List[float]

@app.get("/")
def read_root():
    return {"message": "API de predicción de consumo eléctrico VAR funcionando"}

@app.post("/model_predict")
async def model_predict(file: UploadFile = File(...)):
    """
    Nuevo endpoint: recibe un CSV como archivo (como el que estás enviando con curl)
    """
    logging.info(f"Archivo recibido: {file.filename}")

    # Preprocesar y predecir
    df = load_and_preprocess_data(file, target)
    preds = predict_with_var(df, FORECAST_HORIZON)

    output_path = "data/processed/data_20251026_predicciones.csv"
    preds.to_csv(output_path, index=True)
    logging.info(f"Predicciones guardadas en {output_path}")

    # 4️⃣ Devolver CSV directamente
    return FileResponse(
        path=output_path,
        media_type="text/csv",
        filename="data_20251026_predicciones.csv"
    )