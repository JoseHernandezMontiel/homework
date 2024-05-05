FROM python:3-alpine

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /code

ENV PYTHONPATH "${PYTHONPATH}:/code"

ENV FLASK_APP=/code/src/app.py

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080"]