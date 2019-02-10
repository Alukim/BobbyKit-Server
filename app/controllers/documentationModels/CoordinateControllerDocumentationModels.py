from app import coordinateControllerNamespace
from flask_restplus import fields

distanceResponseModel = coordinateControllerNamespace.model('Distance response model', {
    'distance': fields.Float('Distance')
})