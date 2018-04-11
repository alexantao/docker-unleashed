import logging
import datetime

from flask import Flask, request
from logging.handlers import RotatingFileHandler
from flask.ext.redis import FlaskRedis


app = Flask(__name__)
app.config['REDIS_URL'] = "redis://redis:6379/0"

redis_store = FlaskRedis(app)

handler = RotatingFileHandler('/tmp/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

redis_store.set('Start Time', datetime.datetime.now())


@app.route("/")
def hello():
    app.logger.error(('O Referrer foi: {}'.format(request.referrer)))
    return " ------ > Aplicação com Redis ! <----- "
