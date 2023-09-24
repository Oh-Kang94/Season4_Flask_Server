from flask_jwt_extended import decode_token
from ..config.Config import db
from ..models.DBModel import User

class Auth_Service:
    @staticmethod
    def decode_token(header):
        try:
            # 'Bearer' 부분을 제외한 토큰만 추출
            token = header.split()[1]
            # 토큰 디코딩
            decoded_token = decode_token(token)
            return decoded_token
        except Exception as e:
            print(f"Error decoding token: {e}")
            return None
        
    @staticmethod
    def set_refreshtoken(email, refreshtoken):
        user = User.query.filter_by(email=email).first()
        user.refreshtoken = refreshtoken
        db.session.commit()
        return True