import os
import csv
import pandas as pd
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_tweets(csv_path:str="data/tweets.csv", num_tweets_load:int=10) -> np.array:
  try:
    with open(file=csv_path, mode='r') as file:
      reader = csv.reader(file)
      data = list(reader)

    dataset = np.array(object=data)

    if num_tweets_load > 0 and num_tweets_load < len(dataset):
      tweets = dataset[1:num_tweets_load+1,0:2]
    else:
      tweets = dataset[1:,0:2]

    tweets[:,1] = ''

    return tweets
  except Exception as e:
    print(f"Se ha presentado un error en get_tweets: {e}")

  return None

def analyze_tweet(tweet: str) -> str:
  client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  if tweet:
    person = "Eres un psicologo experto en comportamiento humano, quien analiza tweets de diferentes usuarios para determinar patrones de conducta."
    instruction = f"Analiza el siguiente tweet {tweet}, clasificalo en una de las siguientes categorías: positivo, negativo o neutral de acuerdo a la redacción, contexto y tono del mensaje, sin dar una respuesta extensa, si no lo puedes clasificar, déjalo en blanco."
    context = "Esta clasificación ayudará a identificar el estado de ánimo del usuario y a comprender mejor su patrón de comportamiento."
    format = "Por cada tweet, proporciona una respuesta concisa y simple basada en las categorías de clasificación indicadas."
    audience = "Esta clasificación será analizada por investigadores expertos en conducta humana para poder determinar patrones de comportamiento."

    prompt = person + instruction + context + format + audience

    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "system",
          "content": "Eres un experto en análisis de sentimientos"
        },
        {
          "role": "user",
          "content": prompt
        }
      ]
    )
    return completion.choices[0].message.content
  return None

num_tweets_analyze = st.number_input(label="Cantidad de tweets a analizar:", min_value=0, format="%d", on_change=None)
st_button = None
tweets_array = None
tweets_df = None

if num_tweets_analyze:
  array_tweets = get_tweets(num_tweets_load=num_tweets_analyze)
  df_tweets = pd.DataFrame(data=array_tweets[:,0], columns=["Tweet"])

  st_dataframe = st.dataframe(data=df_tweets, use_container_width=True, hide_index=True)

  st_button = st.button(label="Analizar tweets")

if st_button:
  with st.spinner('Analizando tweets...'):
    for tweet in array_tweets:
      tweet[1] = analyze_tweet(tweet[0])

  st.dataframe(data=pd.DataFrame(data=array_tweets, columns=["Tweet", "Calsificación"]), use_container_width=True, hide_index=True)
