FROM python:3.11

WORKDIR /Proyecto-paises
COPY requirements.txt /Proyecto-paises/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Proyecto-paises/requirements.txt

COPY . /Proyecto-paises/

CMD bash -c "while true, do sleep 1; done"