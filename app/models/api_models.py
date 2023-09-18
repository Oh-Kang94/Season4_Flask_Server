from flask_restx import fields, Namespace

from ..config.Config import api

course_fields = api.namespace('Course').model('Course',{
    'id': fields.Integer(description = 'id', required = True, example = '강의 id'),
    'name': fields.String
})