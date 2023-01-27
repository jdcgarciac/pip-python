#Importar libreria para graficar 
import matplotlib.pyplot as plt
#Generamos una funcion  para graficar
def generate_pie_chart():
    #etiquetas
    labels = ['A', 'B', 'C']
    #valores
    values = [200, 34, 120]
    #Obtener figuras y coorrdenadas
    fig, ax = plt.subplots()
    #Asignar los valores de ejes
    ax.pie(values, labels=labels)
    #Guarda una imagen en formato png en la carpeta graficas
    plt.savefig('graficas/pie.png')
    #Cierra el archivo
    plt.close()