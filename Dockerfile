FROM python:3

WORKDIR /usr/src/app

RUN pip install Flask

EXPOSE 80

COPY . .

CMD [ "python", "./app.py" ]