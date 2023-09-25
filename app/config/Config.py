from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

api = Api(
    title='FLASK RESTful API FOR SEASON4 TEAM2 APP PROJECT For Test',
    version='1.0',
    description='This api for SWIFT Project',
    contact="okh19941994@naver.com",
    license="MIT"
)
db = SQLAlchemy()
jwt = JWTManager()