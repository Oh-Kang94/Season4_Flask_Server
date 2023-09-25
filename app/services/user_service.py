from ..models.DBModel import User
from ..config.Config import db
class UsersService:
    @staticmethod
    def create_user(data):
        new_user = User(
            email=data['email'], 
            password=data['password'], 
            name= data['name'], 
            nickname = data['nickname'],
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def get_user_by_nickname(nickname):
        return User.query.filter_by(nickname=nickname).first()
