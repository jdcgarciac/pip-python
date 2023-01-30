import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#Crear una instancia
app = FastAPI()

#Decorador
@app.get('/')
#Funcion
def get_list():
    return [1,2,3,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
   return """
   <h1>Hola soy una pagina</h1>
   <p>soy un parrafo</p>
   """
#Llama la funcion store
def run():
    store.get_categories()
#Que lo corra como scrip
if __name__ == '__main__':
    run()