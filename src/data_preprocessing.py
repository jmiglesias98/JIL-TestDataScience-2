import pandas as pd
from fastapi import UploadFile
from darts.utils.statistics import remove_seasonality
from darts.utils.utils import SeasonalityMode
from darts.timeseries import TimeSeries

def load_and_preprocess_data(data: UploadFile, target) -> TimeSeries:
    """
    Carga y preprocesa datos para el modelo VAR.
    Puede recibir un DataFrame o una ruta CSV.
    """
    # Si es una ruta, cargar el CSV
    df = pd.read_csv(data.file, parse_dates=True, index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df.asfreq('h')

    # Eliminar filas con NaT en el índice
    df = df[~df.index.isna()]
 
    # Crear serie temporal con Darts
    ts = TimeSeries.from_series(df[target])
    non_seasonal = remove_seasonality(ts[target], model=SeasonalityMode.MULTIPLICATIVE)

    # Combinar con regresores si existen
    df_aux = non_seasonal.to_dataframe()
    df_aux.columns = [target]
    df = pd.concat([df.drop(target, axis = 1), df_aux] , axis = 1)

    return df