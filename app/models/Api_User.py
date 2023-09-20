from flask_restx import fields

from ..config.Config import api

User_fields = api.namespace('User').model('User',{
    'email': fields.String(description='id', required=True, example='id이다.'),
    'refresh_token': fields.String(description='id', required=False, nullable=True, example=None),
    'password': fields.String,
    'name': fields.String,
    'nickname': fields.String,
    'insertdate': fields.String,
    'deletedate': fields.String(required=False, nullable=True, example=None),
})
