FROM python:3.7-buster as builder
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv==2018.11.26
RUN pipenv sync

FROM builder
WORKDIR /app
RUN pipenv shell
CMD ["python", "main.py"]