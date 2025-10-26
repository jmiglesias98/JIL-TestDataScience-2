# JIL-TestDataScience-2

Este repositorio contiene un proyecto de ciencia de datos centrado en analizar y predecir el consumo eléctrico total en la ciudad de Tetuán, Marruecos (Dataset: https://archive.ics.uci.edu/dataset/849/power+consumption+of+tetouan+city). El objetivo principal es modelar cómo las variables ambientales y el histórico de consumo afectan la demanda eléctrica de la ciudad, proporcionando herramientas predictivas que puedan apoyar la planificación energética y la toma de decisiones sobre la gestión de la energía.

El proyecto combina análisis exploratorio de series temporales, construcción y evaluación de modelos multivariantes, y está preparado para un despliegue reproducible mediante contenedores Docker, lo que facilita su integración en entornos productivos y el uso colaborativo.

## Estructura del Proyecto

| Carpeta / Archivo      | Descripción |
|:---------------------:|:------------|
| `notebooks/`           | Contiene notebooks de Jupyter donde se realiza: exploración y limpieza de datos, entrenamiento y validación de modelos de series temporales propuestos.|
| `src/`                 | Scripts y funciones listas para ejecutar el modelo entrenado en un entorno de producción, integrando DevOps mediante contenedores Docker. Incluye la API y utilidades para preprocesar datos y generar predicciones. |
| `models/`              | Contiene el modelo definitivo entrenado, listo para su uso en predicciones o para integrarse en otros entornos. |
| `data/`                | Carpeta para almacenar los datos utilizados en la productivización, organizada en subcarpetas según su estado: por ejemplo, `raw` para datos originales y `processed` para datos preprocesados. |
| `.devcontainer/`       | Configuración de contenedor para asegurar un entorno de desarrollo reproducible, útil para colaborar en el proyecto sin problemas de compatibilidad. |
| `Dockerfile`           | Define la imagen Docker que incluye todas las dependencias y configuraciones necesarias para ejecutar el proyecto de manera consistente. |
| `requirements.txt`     | Lista de bibliotecas de Python con versiones específicas para garantizar compatibilidad y reproducibilidad. |

## Notebooks

| Archivo                     | Descripción |
|-----------------------------|-------------|
| `02_time_series_analysis_test_2.ipynb`    | Notebook que contiene el desarrollo del caso práctico y la argumentación del mismo. |
| `02_time_series_analysis_test_2.html`     | Notebook renderizado. |

## Modelos

| Archivo                     | Descripción |
|-----------------------------|-------------|
  | `var_model_20251026.pkl` | Modelo ganador - VAR. |

## Datos

| Archivo                     | Descripción |
|-----------------------------|-------------|
| `data_20251026.csv` | Fichero sin tratar que utilizaremos como test de nuestro caso práctico. |
| `data_20251026_predicciones.csv` | Salida obtenida de la ejecución del modelo productivizado. |

## Devops

| Archivo                     | Descripción |
|-----------------------------|-------------|
| `main.py`                   | Orquestador de la solución. |
| `data_preprocessing.py`     | Script encargado de cargar los datos y tratarlos para que puedan ser usados por el modelo.|
| `model_predict.py`          | Script encargado de cargar el modelo y realizar la predicción. |
| `config.py`                 | Contiene todos los parámetros a utilizar en nuestra operativización. |


## Instalación y ejecución con docker

| Paso | Comando |
|:----:|:-------|
| Descargar repositorio zip y descomprimir | `-` |
| Posicionarse en el directorio del proyecto | `cd "C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-2-main"` |
| Construir la imagen Docker | `docker build -t jil-testdatascience-2 .` |
| Ejecutar el contenedor con la aplicación | `docker run -it --rm -p 8000:8000 jil-testdatascience-2 uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload` |
| Realizar predicciones sobre un CSV de clientes | `curl -X POST "http://localhost:8000/model_predict" ^ -F "file=@C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-2-main\data\raw\data_20251026.csv" ^ -o "C:\Users\Juanmi Iglesias\Desktop\JIL-TestDataScience-2-main\data\processed\data_20251026_predicciones.csv"` |

NOTA: Se debe sustituir C:\Users\Juanmi Iglesias\Desktop\ por la ruta en la que cada uno vaya a trabajar.

## Requisitos

- Python 3.8 o superior
- Docker
