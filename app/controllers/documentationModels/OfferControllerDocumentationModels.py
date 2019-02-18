from app import offerControllerNamespace
from flask_restplus import fields

parameterModel = offerControllerNamespace.model('Parameter model', {
    'key': fields.String('Key'),
    'value': fields.String('Value')
})

offerDetailsModel = offerControllerNamespace.model('Offer Details model', {
    'imageId': fields.Integer('Id of user image'),
    'category' : fields.String('Category'),
    'name' : fields.String('Name of offer'),
    'pricePerDay' : fields.Float('Price per day'),
    'bail' : fields.Float('Bail'),
    'description' : fields.String('Description'),
    'parameters' : fields.List(fields.Nested(parameterModel)),
    'city' : fields.String('City'),
    'longitude' : fields.Float('Longitude'),
    'latitude' : fields.Float('Latitude'),
    'availabilityOn' : fields.Integer('Availability On'),
})

offerModel = offerControllerNamespace.model('Offer model', {
    'offer' : fields.Nested(offerDetailsModel)
})

bookToolModel = offerControllerNamespace.model('Book tool model', {
    'bookedFor': fields.Integer('BookedFor')
})

availabilityModel = offerControllerNamespace.model('Availability model', {
    'bookedFor': fields.Integer('BookedFor'),
    'isBooked': fields.Boolean('Is Booked'),
    'userId': fields.Integer('User id')
})

offerResponseModel = offerControllerNamespace.model('Offer response model', {
    'imageId': fields.String('Id of user image'),
    'category' : fields.String('Category'),
    'name' : fields.String('Name of offer'),
    'pricePerDay' : fields.Float('Price per day'),
    'bail' : fields.Float('Bail'),
    'description' : fields.String('Description'),
    'parameters' : fields.List(fields.Nested(parameterModel)),
    'city' : fields.String('City'),
    'longitude' : fields.Float('Longitude'),
    'latitude' : fields.Float('Latitude'),
    'availabilityOn' : fields.Integer('Availability On'),
    'availability': fields.Nested(availabilityModel)
})