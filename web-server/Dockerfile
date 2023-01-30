#Version de python en la cual se corre el contenedor
FROM python:3.11

#Aplicacion del directorio
WORKDIR /app
#Actualizacion de requerimientos
COPY requirements.txt /web-server/requirements.txt
#Intalar dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

