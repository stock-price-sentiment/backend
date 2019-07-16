FROM python:3.7.4-stretch
WORKDIR /code
ENV FLASK_APP server.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["uwsgi", "app.ini"]