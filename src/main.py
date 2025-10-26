import logging
from src.config import DATA_PATH, OUTPUT_PATH
from src.data_preprocessing import load_and_preprocess_data
from src.model_predict import predict_with_var

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Iniciando pipeline VAR")

    # 1. Cargar y preparar datos
    logging.info("Cargando y preprocesando datos...")
    ts = load_and_preprocess_data(DATA_PATH)

    # 2. Generar predicciones
    logging.info("Generando predicciones...")
    preds = predict_with_var(ts, FORECAST_HORIZON)

    # 3. Guardar resultados
    preds.to_csv(OUTPUT_PATH)
    logging.info(f"Predicciones guardadas en {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
