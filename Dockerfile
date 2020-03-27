FROM python:3.7-buster as builder
WORKDIR /tmp
COPY Pipfile.lock .
RUN pip install pipenv==2018.11.26
RUN pipenv run pip freeze > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

FROM builder
WORKDIR /app
CMD ["python", "main.py"]