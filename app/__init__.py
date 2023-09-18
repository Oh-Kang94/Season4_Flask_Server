#-*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from .config.Config import api, db
from .config.DBConfig import DBConfig
from .controller.controller import register_namespaces

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(DBConfig)
api.init_app(app)
db.init_app(app)
register_namespaces(api)


if __name__ == "__main__":
    app.run()