from flask_restx import Resource, fields
from ..config.Config import api
from ..services.user_service import UsersService

def user_routes(user_ns):
    @user_ns.route('/registration')
    class Register(Resource):
        @user_ns.doc(
            description = '회원가입',
            responses={
            400: 'User already exists',
            200: 'User created successfully',
        })
        @user_ns.expect(api.model('Register', {
            'email': fields.String(description='ID로 쓰임', example = 'okh19941994@naver.com'),
            'password': fields.String(description='비밀번호', example = 'qwer1234'),
            'name': fields.String(description='사용자 이름', example = '오강현'),
            'nickname': fields.String(description='사용자 닉네임', example = 'Oh-Kang94'),
        }))
        
        def post(self):
            data = api.payload
            email = data['email']
            if UsersService.get_user_by_email(email):
                return {'message': 'User already exists'}, 400

            new_user = UsersService.create_user(data)
            return {'message': 'User created successfully', 'email': new_user.email}, 200
    
    @user_ns.route('/email/<string:email>')
    class findEmail(Resource):
        @user_ns.doc(
            description = '아이디 중복 확인',
            responses={
            400: 'Email Duplicated',
            200: 'Success',
        })
        def get(self, email):
            if UsersService.get_user_by_email(email):
                return {'message': 'Email Duplicated'}, 400
            return {'message': 'Success'}, 200
        
    @user_ns.route('/nickname/<string:nickname>')
    class findNickname(Resource):
        @user_ns.doc(
            description = '닉네임 중복 확인',
            responses={
            400: 'Nickname Duplicated',
            200: 'Success',
        })
        def get(self, nickname):
            if UsersService.get_user_by_nickname(nickname):
                return {'message': 'Nickname Duplicated'}, 400
            return {'message': 'Success'}, 200