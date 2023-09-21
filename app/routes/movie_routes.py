from flask_restx import Resource, fields, abort
from ..models.ApiModel import Movie_fields
from ..services.movie_service import MoiveService
from ..config.Config import api

def movie_routes(movie_ns):
    @movie_ns.route('/create')
    class CreateMovie(Resource):
        @movie_ns.doc(
            description = '달에 한번 csv를 통한 영화 DB 저장.',
            responses={
            500: "Failed to create movies"
        })
        def get(self):
            result = MoiveService.create_movie()
            if result:
                return {'message': 'Movies created successfully'}, 200
            else:
                return {'message': 'Failed to create movies'}, 500

    @movie_ns.route('/get')
    class CreateMovie(Resource):
        @movie_ns.doc(
            description = '영화 리스트 불러오기.',
            responses={
            500: "Failed to get movies"
        })
        @api.marshal_with(Movie_fields)
        def get(self):
            result = MoiveService.get_movie()
            if result:
                return {'result': result}, 200
            else:
                return {'message': 'Failed to get movies'}, 500