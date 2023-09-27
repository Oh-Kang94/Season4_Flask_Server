from flask_restx import Resource, fields
from ..services.auth_service import Auth_Service
from flask import request
from ..config.Config import api
from ..services.user_service import UsersService
from flask_jwt_extended import jwt_required

def user_routes(user_ns, auth_ns):
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
        

        @jwt_required()
        @auth_ns.doc(security='Bearer')
        @user_ns.doc(
            description='닉네임 변경',
            responses={
                401: 'Invalid token',
                400: 'Missing Authorization header',
                200: 'Nickname updated successfully',
                300: 'Server Error'
            })
        @user_ns.expect()
        def put(self, nickname):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                    user_email = decoded_token.get('sub')
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 400
            if UsersService.update_nickname(user_email, nickname):
                return {'message': 'Nickname updated successfully'}, 200
            else:
                return {'message': 'Server Error'}, 300
    
    @user_ns.route('/password')
    class changePassword(Resource):
        @user_ns.doc(
            description = '패스워드 변경',
            responses={
            401: 'Invalid token',
            400: 'Missing Authorization header',
            200: 'User updated successfully',
            403: 'Wrong Password'
        })
        @user_ns.expect(api.model('Password', {
            'current': fields.String(description='현재 비밀번호', example = 'asdjifnaisndfoiajsdfjaosdjfdsa'),
            'new': fields.String(description='신 비밀번호', example = 'dsjfnjklnfdjglsnlkfjiwesfidnfilss'),
        }))
        @jwt_required()
        @auth_ns.doc(security='Bearer')
        def put(self):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                    user_email = decoded_token.get('sub')
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 400
            data = api.payload
            currentPW = data['current']
            newPW = data['new']
            if UsersService.update_password(user_email,currentPW,newPW ):
                return {'message': 'User updated successfully'}, 200
            else:
                return {'message': 'Wrong Password'}, 403