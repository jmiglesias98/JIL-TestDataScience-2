from pathlib import Path

# Rutas principales
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "var_model_20251026.pkl"
DATA_PATH = BASE_DIR / "data" / "daily_input.csv"
OUTPUT_PATH = BASE_DIR / "data/processed/" / "predictions.csv"

# Parámetros del modelo / forecast
FORECAST_HORIZON = 100

# Variable objetivo
target = 'Total Power Consumption'