from app import offerControllerNamespace
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel
from app.controllers.parsers.AccountControllerParsers import AccountControllerParsers
from app.controllers.documentationModels.AccountControllerDocumentationModels import userResponseModel, userRegistrationModel, userLoginModel, token_model
from app.controllers.documentationModels.ErrorDocumentionModels import error_model
from app.controllers.responses.ErrorResponses import errorMessage
from app.controllers.responses.TokenResponseModel import TokenResponseModel 
from app.controllers.responses.UserResponseModels import userResponseModels
from flask import jsonify
from flask_restplus import Resource, marshal_with
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.controllers.parsers.OfferControllerParsers import offerControllerParsers
from app.controllers.documentationModels.OfferControllerDocumentationModels import offerModel
from app.models.Offer import Offer
from app.models.Parameter import Parameter
from app.models.Availability import Availability
from app import ma

class OfferSchema(ma.ModelSchema):
    parameters = ma.Nested('ParameterSchema', many=True, exclude=('offer',))
    availability = ma.Nested('AvailabilitySchema', many=False, exclude=('offer',))
    class Meta:
        model = Offer

class ParameterSchema(ma.ModelSchema):
    class Meta:
        model = Parameter

class AvailabilitySchema(ma.ModelSchema):
    class Meta:
        model = Availability

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class OffersController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    @offerControllerNamespace.expect(offerModel)
    def post(self):
        command = offerControllerParsers.createUpdateOfferParser.parse_args()
        details = offerControllerParsers.offerDetailsParser.parse_args(req=command)

        if not details.pricePerDay > 0:
            return {'message': "Price per day must be greater than 0"}, 400

        if not details.bail > 0:
            return {'message': "Bail must be greater than 0"}, 400

        if not details.availabilityOn > 0:
            return {'message': "Availability On must be greater than 0"}, 400

        userId = get_jwt_identity()

        newOffer = Offer(
            userId = userId
        )

        newOffer.create(details)

        return {'id': newOffer.id}, 201

    def get(self):
        


@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class OfferController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    @offerControllerNamespace.expect(offerModel)
    def patch(self, id):
        command = offerControllerParsers.createUpdateOfferParser.parse_args()
        details = offerControllerParsers.offerDetailsParser.parse_args(req=command)

        if not details.pricePerDay > 0:
            return {'message': "Price per day must be greater than 0"}, 400

        if not details.bail > 0:
            return {'message': "Bail must be greater than 0"}, 400

        if not details.availabilityOn > 0:
            return {'message': "Availability On must be greater than 0"}, 400

        userId = get_jwt_identity()

    def get(self, id):
        offer = Offer.findOfferById(id)
        return offer_schema.jsonify(offer)

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class UserOfferController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    def get(self):
        userId = get_jwt_identity()

        offers = Offer.findOffersByUserId(userId)

        offer_schema = OfferSchema(many=True)
        return offer_schema.jsonify(offers)

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class BookingOfferController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    def patch(self, id):
        userId = get_jwt_identity()

        offer = Offer.findOfferById(id)

        if not offer:
            return {'message': 'Offer does not exist'}, 400

        if offer.userId == userId:
            retrun {'message': 'Cannot booked yourself tool'}, 400

        if offer.availability.isBooked:
            return {'message': 'Offer is already booked'}, 400

        offer.bookTool(userId)
        return {'id': offer.id}, 204