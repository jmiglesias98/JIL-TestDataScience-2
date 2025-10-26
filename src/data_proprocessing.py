import pandas as pd
from darts.dataprocessing.transformers import remove_seasonality
from darts import TimeSeries

def load_and_preprocess_data(csv_path: str) -> TimeSeries:

    # Cargar datos 
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    ts = TimeSeries.from_dataframe(df[target])

    # Remover estacionalidad
    ts_deseasonalized = remove_seasonality(ts[target],model=SeasonalityMode.ADDITIVE)
    
    # Unir la serie desestacionalida con los regresores
	df_aux = ts_deseasonalized.to_dataframe()
	df_aux.columns = [target]
	df = pd.concat([df.drop(target, axis = 1), df_aux] , axis = 1)

    return ts_deseasonalized
