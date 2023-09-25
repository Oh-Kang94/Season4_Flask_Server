from flask_restx import Resource
from ..config.Config import api
from ..services.user_service import UsersService
from ..models.ApiModel import User_fields

def user_routes(user_ns):
    @user_ns.route('/registration')
    class Register(Resource):
        @api.expect(User_fields)
        @user_ns.doc(description = '회원 가입',)  
        def post(self):
            data = api.payload
            email = data['email']
            if UsersService.get_user_by_email(email):
                return {'message': 'User already exists'}, 400

            new_user = UsersService.create_user(data)
            return {'message': 'User created successfully', 'email': new_user.email}, 200