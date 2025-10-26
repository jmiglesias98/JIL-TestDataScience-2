import joblib
import pandas as pd
from sktime.forecasting.base import ForecastingHorizon

from src.config import MODEL_PATH, FORECAST_HORIZON

def predict_with_var(ts, steps: int = FORECAST_HORIZON) -> pd.DataFrame:
    
    model = joblib.load(MODEL_PATH)

    # Horizonte de predicción
    fh = ForecastingHorizon(range(1, steps + 1))
    
    # Actualizamos el modelo con los nuevos datos
    model.update(ts)

    # Predicción
    y_pred = model.predict(fh=fh)

    # Convertir a DataFrame si es necesario
    if hasattr(y_pred, "to_pandas"):
        y_pred = y_pred.to_pandas()

    return y_pred