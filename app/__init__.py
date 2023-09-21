#-*- coding: utf-8 -*-
from dotenv import load_dotenv
import os 
from flask import Flask
from flask_cors import CORS
from .config.Config import api, db, jwt
from .config.DBConfig import DBConfig
from .controller.controller import register_namespaces
import warnings

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config.from_object(DBConfig)
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 30 * 24 *  60 * 60
# app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 
app.config["JWT_SECRET_KEY"] = os.environ.get('JWT_SECRET_KEY')
api.init_app(app)
db.init_app(app)
jwt.init_app(app)
register_namespaces(api)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app.run()