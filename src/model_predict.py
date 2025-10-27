import joblib
import pandas as pd
from sktime.forecasting.base import ForecastingHorizon
from src.config import MODEL_PATH, FORECAST_HORIZON

def predict_with_var(df, steps: int = FORECAST_HORIZON) -> pd.DataFrame:
    df.index = pd.to_datetime(df.index)
    df = df.asfreq('H')

    model = joblib.load(MODEL_PATH)

    model.fit(df)

    fh = ForecastingHorizon(range(1, steps + 1), is_relative=True, freq='H')

    y_pred = model.predict(fh=fh)

    if hasattr(y_pred, "to_pandas"):
        y_pred = y_pred.to_pandas()

    return y_pred
