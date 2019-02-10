from app import api
from flask_restplus import fields

error_model = api.model('Error model', {
    'message': fields.String('Message')
})