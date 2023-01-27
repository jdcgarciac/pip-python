from excel import *
from utils import *
from charts import *


def run():
  data = read_csv('./Proyecto-paises/data.csv') #Ubicacion carpeta archivo
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  generate_pie_chart(countries, percentages)

if __name__ == '__main__':
  run()