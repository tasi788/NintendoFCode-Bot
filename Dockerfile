FROM python:3.7-buster as builder
WORKDIR /tmp
RUN pip install pipenv==2018.11.26
RUN pipenv run pip freeze > requirements.txt
RUN pip install -r requirements.txt

FROM builder
WORKDIR /app
CMD ["python", "main.py"]