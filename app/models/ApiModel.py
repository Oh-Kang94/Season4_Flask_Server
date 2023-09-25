from flask_restx import fields

from ..config.Config import api

User_fields = api.namespace('User').model('User', {
    'email': fields.String(description='Email', example='user@example.com'),
    'refreshtoken': fields.String(description='Refresh Token', required=False, nullable=True, example=None),
    'password': fields.String(description='Password'),
    'name': fields.String(description='Name'),
    'nickname': fields.String(description='Nickname'),
    'insertdate': fields.String(description='Insert Date', required=False, nullable=True, example='2000.01.01'),
    'deletedate': fields.String(description='Delete Date', required=False, nullable=True, example='2000.01.01'),
})

Movie_fields = api.namespace('movie').model('movie', {
    'id': fields.Integer(description='ID', example=1),
    'ott': fields.String(description='OTT', example='Netflix'),
    'title': fields.String(description='Title', example='Inception'),
    'imagepath': fields.String(description='Image Path', example='/path/to/image.jpg'),
    'releasedate': fields.String(description='Release Date', example='2023-09-21'),
    'genre': fields.String(description='Genre', example='Science Fiction'),
    'totalaudience': fields.Integer(description='Total Audience', example=1000000),
    'country': fields.String(description='Country', example='USA'),
    'rating': fields.String(description='Rating', example='PG-13'),
    'star': fields.Float(description='Star', example= 4.5),
    'runningtime': fields.Integer(description='Running Time', example=150),
    'summary': fields.String(description='Summary', example='A mind-bending thriller about dreams and reality.'),
})

Cast_fields = api.namespace('cast').model('cast', {
    'id': fields.Integer(description='ID', example=1),
    'imgpath': fields.String(description='Image Path', example='/path/to/image.jpg'),
    'name': fields.String(description='Name', example='Leonardo DiCaprio'),
    'role': fields.String(description='Role', example='Cobb'),
})

Review_fields = api.namespace('Review').model('Review', {
    'user_email': fields.String(description='User Email', example='user@example.com'),
    'movie_id': fields.Integer(description='Movie ID', example=1),
    'content': fields.String(description='Content'),
    'rating': fields.Float(description='Rating', example=4.5),
    'insertdate': fields.String(description='Insert Date', example='2023.09.21'),
    'deletedate': fields.String(description='Delete Date', required=False, nullable=True, example=None),
})

ReviewWrite_fields= api.namespace('Review').model('Review', {
    'user_email': fields.String(description='User Email', example='okh19941994@naver.com'),
    'movie_id': fields.Integer(description='Movie ID', example=1),
    'content': fields.String(description='Content', example='재미있어요.'),
    'rating': fields.Float(description='Rating', example=4.5),
})

Login_fields = api.namespace('Auth').model('Auth', {
    'email': fields.String(required=True, example='okh19941994@naver.com'),
    'password': fields.String(required=True, example='1234')
})

