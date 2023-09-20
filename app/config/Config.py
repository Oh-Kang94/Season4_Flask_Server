from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager



api = Api(
    title='FLASK RESTful API FOR SEASON4 TEAM2 APP PROJECT',
    version='1.0',
    description='This api for SWIFT Project',
    contact="okh19941994@naver.com",
    license="MIT"
)
db = SQLAlchemy()
jwt = JWTManager()