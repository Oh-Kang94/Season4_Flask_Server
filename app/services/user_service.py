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
    
    @staticmethod
    def get_nickname_by_email(email):
        return User.query.filter_by(email=email).first().nickname
    
    @staticmethod
    def update_nickname(email, new_nickname):
        # 이메일을 기반으로 사용자를 찾습니다.
        user = User.query.filter_by(email=email).first()

        if user:
            # 사용자가 존재하면 닉네임을 업데이트하고 저장합니다.
            user.nickname = new_nickname
            db.session.commit()
            return True
        else:
            return False