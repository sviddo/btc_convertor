FROM python:3

WORKDIR /app

COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt 

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:80