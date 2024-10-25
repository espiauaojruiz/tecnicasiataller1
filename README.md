## Taller 1
Se plantea un clasificador de sentimientos, usando el modelo **gpt-4o de OpenAI**, y el [dataset](https://huggingface.co/datasets/mrm8488/tass-2019).

En un navegador web se cargará la aplicación, dónde deberá escoger la cantidad de tweets a analizar, los cuales se cargaran en una tabla junto con un botón (Analizar Tweets), el cuál al darle click hará uso de la API de OpenAI para realizar el análisis y clasificación de los tweets cargados, mostrando otra tabla debajo del botón con los tweets analizados y la clasificación de cada uno dada por el modelo, se especifica en el prompt del modelo que se debe clasificar los tweets en una de las siguientes categgorías *Positivo*, *Negativo*, *Neutro*

### Estructura del proyecto
```
/Proyecto
│
├── /data
│   │
│   └── tweets.py
│
├── requirements.txt
│
└── app.py
```

### Requisitos
* Python 3.8+
* En el diractorio raíz del proyecto crear el archivo ```.env``` en el cual se deberá especificar el API key con la clave ```OPENAI_API_KEY```
* Instalación de las dependencias, desde el diractorio raíz del proyecto ejecutar el comando ```pip install -r requirements.txt```

### Uso
* Desde el diractorio raíz del proyecto ejecutar el comando ```streamlit run app.py```
