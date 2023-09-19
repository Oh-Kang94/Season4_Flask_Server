from flask_restx import Resource
from ..services.user_service import HelloService, UsersService
from ..models.Api_User import User_fields

def user_routes(ns):
    @ns.route("/hello")
    class Hello(Resource):
        @ns.response(200, 'success', User_fields)
        @ns.response(500, 'Fail', User_fields)
        def get(self):
            return HelloService.get_hello(), 200

    @ns.route("/user")
    class Courses(Resource):
        @ns.marshal_list_with(User_fields)
        @ns.response(200, 'success', User_fields)
        @ns.doc(response = {400 : 'Cannot find User'})
        def get(self):
            return UsersService.get_users(), 200
