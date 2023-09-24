from flask_restx import Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from ..config.Config import api
from ..services.user_service import UsersService
from ..services.auth_service import Auth_Service
from ..models.ApiModel import Login_fields

def auth_routes(auth_ns):
    @auth_ns.route('/')
    class Login(Resource):
        @api.expect(Login_fields)
        @auth_ns.doc(description = '로그인 하는 route',)  
        def post(self):
            data = api.payload
            email = data['email']
            password = data['password']

            user = UsersService.get_user_by_email(email)
            if user and user.password == password:
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                Auth_Service.set_refreshtoken(refreshtoken=refresh_token,email=email)
                return {
                    'message': 'Logged in successfully',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            return {'message': 'Invalid credentials'}, 401
    @auth_ns.route('/getaccess')
    class Refresh(Resource):
        @jwt_required(refresh=True)
        @auth_ns.expect(api.model('refresh_token', {
            'refresh_token': fields.String(description='header에 refresh_token넣어줘야함.', example = 'asdjfnasj2ij123jacnjadsnasdfnj')
        }))
        @auth_ns.doc(security = 'Bearer', description = 'ACCESS_TOKEN을 발급 받기 위함.',)  
        def post(self):
            current_user = get_jwt_identity()
            new_access_token = create_access_token(identity=current_user)
            return {'access_token': new_access_token}, 200