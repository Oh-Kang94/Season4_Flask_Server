from flask_restx import Resource
from ..config.Config import api
from ..services.user_service import UsersService
from ..models.ApiModel import User_fields

def user_routes(user_ns):
    @user_ns.route('/register')
    class Register(Resource):
        @api.expect(User_fields)
        def post(self):
            data = api.payload
            email = data['email']

            if UsersService.get_user_by_email(email):
                return {'message': 'User already exists'}, 400

            new_user = UsersService.create_user(data)
            return {'message': 'User created successfully', 'email': new_user.email}, 201