from flask_restx import Resource, Namespace

from .models.models import User
from .models.api_models import course_fields

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    @ns.response(200,'Fail',course_fields)    
    @ns.response(500,'success',course_fields)    
    def get(self):
        """인사 입니다."""
        return {"Hello": "안녕"}, 500


@ns.route("/courses")
class Courses(Resource):
    @ns.marshal_list_with(course_fields)
    @ns.response(200,'success',course_fields)    
    def get(self):

        return User.query.all(), 200
