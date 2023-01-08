FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /django-assessment-stefan-cosma
COPY requirements.txt /django-assessment-stefan-cosma/
RUN pip install -r requirements.txt
COPY . /django-assessment-stefan-cosma/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 