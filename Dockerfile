FROM alpine:3.6

RUN apk add --no-cache python py2-pip curl

WORKDIR /usr/src
COPY requirements.txt /usr/src
COPY app.py /usr/src/

ENV FLASK_APP=app.py

RUN pip install -r /usr/src/requirements.txt
EXPOSE 5000

HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1

ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]
