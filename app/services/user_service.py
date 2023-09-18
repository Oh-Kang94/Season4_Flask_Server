from ..models.User import User

class HelloService:
    @staticmethod
    def get_hello():
        return {"Hello": "안녕"}

class UsersService:
    @staticmethod
    def get_users():
        return User.query.all()
