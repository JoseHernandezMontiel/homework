FROM python:3-alpine

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/code/src/app.py"]

# RUN pip install -e src

# CMD ["pytest"]