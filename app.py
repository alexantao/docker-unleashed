import logging
from flask import Flask, request
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

handler = RotatingFileHandler('/tmp/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

@app.route("/")
def hello():
    app.logger.error(('O Referrer foi: {}'.format(request.referrer)))
    return " ------ > Olá. Mundo (versão 2)! <----- "
