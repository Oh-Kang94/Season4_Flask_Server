from flask_restx import Resource, marshal, fields
from flask import request
from ..models.ApiModel import Review_fields, ReviewWrite_fields, Review_field_result
from ..services.review_service import ReviewService
from ..services.user_service import UsersService
from ..services.auth_service import Auth_Service
from ..config.Config import api
from flask_jwt_extended import jwt_required


def review_routes(review_ns, auth_ns):
    @review_ns.route('/')
    class CreateReview(Resource):
        @jwt_required()
        @review_ns.doc(
            description='리뷰작성.',
            responses={
                401: 'Invalid token',
                400: 'Missing Authorization header',
                200: 'Success',
                500: 'Already wrote Review',
            })
        @auth_ns.doc(security='Bearer')
        @review_ns.expect(api.model('CreateReview', {
            'movie_id': fields.String(description='movie_id integer', example='3'),
            'content': fields.String(description='영화의 리뷰 내용', example='영화가 재미있습니다.'),
            'rating': fields.String(description='영화의 평점으로 Rating', example='9.8'),
        }))
        def post(self):
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
            data = request.get_json()
            movie_id = data.get('movie_id')
            content = data.get('content')
            rating = data.get('rating')

            result = ReviewService.create_review(
                user_email, movie_id, content, rating)
            if result:
                return {'message': 'Review created successfully', 'result': marshal(result, Review_fields)}, 200
            else:
                return {'message': 'Already wrote Review'}, 500

    @review_ns.route('/<int:movie_id>')
    class CRUDReview(Resource):
        @review_ns.doc(
            description='영화별 리뷰 가져오기.',
            responses={
                401: 'Review not found',
                200: 'Success',
            })
        def get(self, movie_id):
            result = ReviewService.get_review_all(movie_id)
            if result:
                updated_result = []

                for review in result:
                    nickname = UsersService.get_nickname_by_email(
                        review.user_email)
                    transformed_review = {
                        'nickname': nickname,
                        'movie_id': review.movie_id,
                        'content': review.content,
                        'rating': review.rating,
                        'insertdate': review.insertdate,
                        'deletedate': review.deletedate
                    }
                    updated_result.append(transformed_review)
                return {'result': marshal(updated_result, Review_field_result)}, 200
            else:
                return {'message': 'Review not found'}, 400

        @jwt_required()
        @auth_ns.doc(security='Bearer')
        @review_ns.doc(
            description='리뷰 수정하기',
            responses={
                401: 'Invalid token',
                400: 'Missing Authorization header',
                200: 'Review updated successfully',
                500: 'Review not found',
            })
        @review_ns.expect(api.model('UpdateReview', {
            'content': fields.String(description='영화의 리뷰 내용', example='영화가 재미있습니다.'),
            'rating': fields.String(description='영화의 평점으로 Rating', example='9.8'),
        }))
        def put(self, movie_id):
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

            data = request.get_json()
            content = data.get('content')
            rating = data.get('rating')

            result = ReviewService.update_review(
                user_email, movie_id, content, rating)
            if result:
                return {'message': 'Review updated successfully'}, 200
            else:
                return {'message': 'Review not found'}, 500

        @jwt_required()
        @auth_ns.doc(security='Bearer')
        @review_ns.doc(
            description='리뷰 수정하기',
            responses={
                401: 'Invalid token',
                400: 'Missing Authorization header',
                200: 'Review deleted successfully',
                500: 'Review not found',
            })
        def delete(self, movie_id):
            authorization_header = request.headers.get('Authorization')
            if authorization_header and authorization_header.startswith('Bearer '):
                decoded_token = Auth_Service.decode_token(authorization_header)
                if decoded_token:
                    # 여기서 'sub'는 사용자의 이메일 주소를 의미합니다.
                    user_email = decoded_token.get('sub')
                else:
                    return {'message': 'Invalid token'}, 401
            else:
                return {'message': "Invalid or missing Authorization header"}, 401

            result = ReviewService.delete_review(user_email, movie_id)
            if result:
                return {'message': 'Review deleted successfully'}, 200
            else:
                return {'message': 'Review not found'}, 500
