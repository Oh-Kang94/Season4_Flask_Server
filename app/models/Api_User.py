from flask_restx import fields

from ..config.Config import api

User_fields = api.namespace('User').model('User',{
    'id': fields.String(description = 'id', required = True, example = 'id이다.'),
    'name': fields.String
})