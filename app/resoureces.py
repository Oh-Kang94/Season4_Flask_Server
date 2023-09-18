from flask_restx import Resource, Namespace

from .models.User import User
from .models.Api_User import User_fields

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    @ns.response(200,'Fail',User_fields)    
    @ns.response(500,'success',User_fields)    
    def get(self):
        """인사 입니다."""
        return {"Hello": "안녕"}, 500


@ns.route("/courses")
class Courses(Resource):
    @ns.marshal_list_with(User_fields)
    @ns.response(200,'success',User_fields)    
    def get(self):

        return User.query.all(), 200
