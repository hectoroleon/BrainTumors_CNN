# BrainTumors_CNN
Este repositorio contiene el código y recursos del proyecto final de la clase "Proyecto de Ciencia de Datos".

La estructura del repositorio es la siguiente:
 
BrainTumors_CNN/

- Informe/
  - RicardoHernandez_HectorOrnelas.ipynb (Informe escrito del proyecto)
- Data/
  - Raw/
    - glioma_tumor/
    - meningioma_tumor/
    -  normal/
    - pituitary_tumor/
  - Prepared/
    - test/
    - train/
    - val/
- Data Wrangling/
   - preparacion_datos.ipynb (Preparación y limpieza de datos)
- EDA/
  - EDA.ipynb (Análisis Exploratorio de Datos)
- API/
  -  main.py (Código principal de la API)
  - Dockerfile (Configuración para Docker)
  - requirements.txt (Listado de dependencias)
- Model/
  - Entrenamiento_y_seleccion_de_modelo.ipynb (Entrenamiento y selección de modelo)

## Descripción de Carpetas y Archivos

- Informe: Contiene el informe final del proyecto que documenta los hallazgos y resultados obtenidos en el análisis de imágenes de resonancia magnética.

- Data:
  - Raw: Incluye imágenes de diferentes tipos de tumores cerebrales para su análisis (glioma_tumor, meningioma_tumor, normal, pituitary_tumor)
  - Prepared: Contiene las divisiones de datos para entrenamiento, prueba y validación del modelo.

- Data Wrangling: Este directorio alberga el cuaderno utilizado para preparar y limpiar los datos antes del análisis.

- EDA (Análisis Exploratorio de Datos): Proporciona un cuaderno para explorar y comprender la naturaleza de los datos.

- API: Contiene los archivos necesarios para implementar una API que pueda utilizar el modelo entrenado para clasificar imágenes de tumores cerebrales.

- Model: Incluye el cuaderno utilizado para entrenar y seleccionar el modelo más adecuado para la clasificación de imágenes.
