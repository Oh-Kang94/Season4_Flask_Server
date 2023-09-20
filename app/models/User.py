from ..config.Config import db


class User(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(50), primary_key=True)
    refreshtoken = db.Column(db.String(200), nullable=True)  # refreshtoken을 nullable로 설정
    password = db.Column(db.String(45))
    name = db.Column(db.String(45))
    nickname = db.Column(db.String(45))
    address = db.Column(db.String(45))
    insertdate = db.Column(db.String(45))
    deletedate = db.Column(db.String(45), nullable=True)  # deletedate를 nullable로 설정
