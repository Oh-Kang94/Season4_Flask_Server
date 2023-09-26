from flask_restx import Resource, fields, abort
from flask import render_template
from ..services.map_service import Map_Service
from ..config.Config import api


def map_routes(map_ns):
    @map_ns.route("/<float:latitude>/<float:longitude>")
    class Find_Theater(Resource):
        @map_ns.expect(api.model('Map', {
            'latitude': fields.Float(description='위도', example = '37.537511'),
            'longitude': fields.Float(description='경도', example = '127.072594')
        }))
        @map_ns.doc(
            description = '영화관 검색\n영화관 검색은 http://www.oh-kang.kro.kr:18712/map/preview 로 참고',
            responses={
            400: "Bad request. need 'review'",
            500: "Cannot find the AI Model"
        })
        def get(self, latitude, longitude):
            if Map_Service.Find_Theater(latitude, longitude):
                return render_template('movie.html')
            else:
                return "Failed to generate cinema map", 500  # 예외 처리