from excel import *
from utils import *
from charts import *
import pandas as pd


def run():
  #leer csv con pandas
  df = pd.read_csv('data.csv')
  #Generar filtros
  df = df[df["Continent"] == 'Africa']
  #Obtener valores de paises
  countries = df["Country"].values
  #Obtener porcentajes de la poblacion
  percentages = df["World Population Percentage"].values
  #Funciones para graficar
  generate_bar_chart(countries, countries)
  generate_pie_chart(countries, percentages)

if __name__ == '__main__':
  run()