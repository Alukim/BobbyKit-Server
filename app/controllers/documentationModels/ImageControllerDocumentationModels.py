from app import imageControllerNamespace
from flask_restplus import fields

uploadImageResponseModel = imageControllerNamespace.model('Image uploaded', {
    'message': fields.Integer()
})