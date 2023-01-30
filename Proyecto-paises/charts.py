#Importa la libreria de graficas
# as permite tener un alias para llamarla de forma mas facil
import matplotlib.pyplot as plt

#Grafico de barras
def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #Guarda una imagen en formato png en la carpeta graficas
  plt.savefig('barras.png')
  #Cierra el archivo
  plt.close()
  
#Grafica de circulos -- torta
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #Guarda una imagen en formato png en la carpeta graficas
  plt.savefig('circulo.png')
  #Cierra el archivo
  plt.close()
