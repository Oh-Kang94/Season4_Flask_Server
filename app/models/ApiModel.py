from flask_restx import fields

from ..config.Config import api

User_fields = api.namespace('User').model('User',{
    'email': fields.String(description='email', required=True),
    'refresh_token': fields.String(description='password', required=False, nullable=True, example=None),
    'password': fields.String,
    'name': fields.String,
    'nickname': fields.String,
    'address': fields.String,
    'insertdate': fields.String,
    'deletedate': fields.String(required=False, nullable=True, example=None),
})

login_fields = api.namespace('Auth').model('Auth', {
    'email': fields.String(required=True, example='okh19941994@navr.com'),
    'password': fields.String(required=True, example='string')
})