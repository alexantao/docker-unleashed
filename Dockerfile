FROM python:3-slim

COPY requirements.txt /usr/src
COPY app.py /usr/src/
ENV FLASK_APP=app.py
RUN pip install -r /usr/src/requirements.txt
WORKDIR /usr/src

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
