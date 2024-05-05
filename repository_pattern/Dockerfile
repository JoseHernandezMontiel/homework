FROM python:3-alpine

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=/code/src/app.py

ENV PYTHONPATH "${PYTHONPATH}:/code/src"

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080"]