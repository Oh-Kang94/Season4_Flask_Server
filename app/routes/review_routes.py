from flask_restx import Resource, marshal
from flask import request
from ..models.ApiModel import Review_fields, ReviewWrite_fields
from ..services.review_service import ReviewService
from ..services.auth_service import Auth_Service
from ..config.Config import api
from flask_jwt_extended import jwt_required

def review_routes(review_ns, auth_ns):
    @review_ns.route('/')
    class CreateReview(Resource):
        @jwt_required()
        @auth_ns.doc(security='Bearer')
        @api.expect(ReviewWrite_fields)  # review_fields 모델을 정의해야 함
        def post(self):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    user_email = decoded_token.get('sub')  # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 401
            data = request.get_json()
            user_email = data.get('user_email')
            movie_id = data.get('movie_id')
            content = data.get('content')
            rating = data.get('rating')

            result = ReviewService.create_review(user_email, movie_id, content, rating)
            if result:
                return {'message': 'Review created successfully', 'result': marshal(result, Review_fields)}, 200
            else:
                return {'message': 'Already wrote Review'}, 500

    @review_ns.route('/<int:movie_id>')
    class GetReview(Resource):
        def get(self, movie_id):
            result = ReviewService.get_review_all(movie_id)
            if result:
                return {'result': marshal(result, Review_fields)}, 200
            else:
                return {'message': 'Review not found'}, 404
        
        @jwt_required()
        @auth_ns.doc(security='Bearer')
        @api.expect(ReviewWrite_fields)  # review_fields 모델을 정의해야 함
        def put(self):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    user_email = decoded_token.get('sub')  # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 401
            
            data = request.get_json()
            movie_id = data.get('movie_id')
            content = data.get('content')
            rating = data.get('rating')

            result = ReviewService.update_review(user_email, movie_id, content, rating)
            if result:
                return {'message': 'Review updated successfully'}, 200
            else:
                return {'message': 'Review not found'}, 404
            
        
        @jwt_required()
        @auth_ns.doc(security='Bearer')
        def delete(self, movie_id):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    user_email = decoded_token.get('sub')  # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 401

            result = ReviewService.delete_review(user_email, movie_id)
            if result:
                return {'message': 'Review deleted successfully'}, 200
            else:
                return {'message': 'Review not found'}, 404