from flask_restx import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from ..config.Config import api
from ..services.user_service import UsersService
from ..models.ApiModel import login_fields

def auth_routes(auth_ns):
    @auth_ns.route('/')
    class Login(Resource):
        @api.expect(login_fields)
        def post(self):
            data = api.payload
            email = data['email']
            password = data['password']

            user = UsersService.get_user_by_email(email)
            if user and user.password == password:
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                UsersService.set_refreshtoken(refreshtoken=refresh_token,email=email)
                return {
                    'message': 'Logged in successfully',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            return {'message': 'Invalid credentials'}, 401

    @auth_ns.route('/checkaccess')
    class Protected(Resource):
        @jwt_required()
        @api.expect(login_fields)
        @auth_ns.doc(security = 'Bearer')  

        def post(self):
            current_user = get_jwt_identity()
            return {'message': f'Hello {current_user}'}

    @auth_ns.route('/getaccess')
    class Refresh(Resource):
        @jwt_required(refresh=True)
        @auth_ns.doc(security = 'Bearer')  
        def post(self):
            current_user = get_jwt_identity()
            new_access_token = create_access_token(identity=current_user)
            return {'access_token': new_access_token}, 200