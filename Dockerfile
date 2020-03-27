FROM python:3.7-buster as builder
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv==2018.11.26
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

FROM builder
WORKDIR /app
CMD ["python", "main.py"]