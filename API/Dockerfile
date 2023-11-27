FROM python:3.10-slim-buster
LABEL authors = "ricardo-hernandez_hector-ornelas"
WORKDIR /API


RUN apt-get update && apt-get install -y procps && pip install -U pip \
    && rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime  \
    && apt-get install libgomp1


COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


COPY main.py /API

EXPOSE 8000
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "8000"]