FROM python:3.6.8


RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD python /app/main.py