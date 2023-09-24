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
            # Movie 먼저 생성
            resultMovie = MoiveService.create_movie()
            
            if resultMovie:
                # Movie 생성이 성공했을 경우에만 Cast 생성
                resultCast = MoiveService.create_cast()
                    
                if resultCast:
                    return {'message': 'Movies and Cast created successfully'}, 200
                else:
                    return {'message': 'Failed to create Cast'}, 500
            else:
                return {'message': 'Failed to create Movies'}, 500

    @movie_ns.route('/get')
    class CreateMovie(Resource):
        @movie_ns.doc(
            description = '영화 리스트 불러오기.',
            responses={
            500: "Failed to get movies"
        })
        def get(self):
            result = MoiveService.get_movie()
            if result:
                return {'result': result}, 200
            else:
                return {'message': 'Failed to get movies'}, 500