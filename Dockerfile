FROM python:3
WORKDIR /django_todoapp
COPY requirements.txt /django_todoapp/
RUN pip install -r requirements.txt
COPY . /django_todoapp/