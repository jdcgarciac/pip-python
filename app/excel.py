#Importar libreria excel
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #Obtener el nombre de las columnas
    #Para obtener las llaves
    header = next(reader)
    data = []
    for row in reader:
      #Unir el array de tuplas
      iterable = zip(header, row)
      #Se genera un diccionario de clave y valor
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data



