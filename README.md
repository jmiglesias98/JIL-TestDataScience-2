# JIL-TestDataScience-2


## Instalación y ejecución con docker

| Paso | Comando |
|:----:|:-------|
| Descargar repositorio zip y descomprimir | `-` |
| Posicionarse en el directorio del proyecto | `cd "C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-1-main"` |
| Construir la imagen Docker | `docker build -t jil-testdatascience-1 .` |
| Ejecutar el contenedor con la aplicación | `docker run -it --rm -p 8000:8000 jil-testdatascience-1 uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload` |
| Realizar predicciones sobre un CSV de clientes | `curl -X POST "http://localhost:8000/predict_csv" ^ -F "file=@C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-1-main\data\raw\clientes_20251016.csv" ^ -o "C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-1-main\data\processed\clientes_20251016_predicciones.csv"` |

NOTA: Se debe sustituir C:\Users\Juanmi Iglesias\Desktop\ por la ruta en la que cada uno vaya a trabajar.

## Requisitos

- Python 3.8 o superior
- Docker
