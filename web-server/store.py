#Libreria Peticiones
import requests
#Funcion de obtener categorias
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    #Estado
    print(r.status_code)
    #Informacion
    print(r.text)
    print(type(r.text))
    #Transformar en JSON -- lista
    categories = r.json()
    #Recorrer la lista por nombre
    for category in categories:
        print(category['name'])
    