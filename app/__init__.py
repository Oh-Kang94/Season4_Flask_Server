#-*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from .config.Config import api, db
from .config.DBConfig import DBConfig
from .resoureces import ns

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(DBConfig)
api.init_app(app)
db.init_app(app)

# api.add_namespace(ns)


if __name__ == "__main__":
    app.run()