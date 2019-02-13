from app import offerControllerNamespace
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel
from app.controllers.parsers.AccountControllerParsers import AccountControllerParsers
from app.controllers.documentationModels.AccountControllerDocumentationModels import userResponseModel, userRegistrationModel, userLoginModel, token_model
from app.controllers.documentationModels.ErrorDocumentionModels import error_model
from app.controllers.responses.ErrorResponses import errorMessage
from app.controllers.responses.TokenResponseModel import TokenResponseModel 
from app.controllers.responses.UserResponseModels import userResponseModels
from flask_restplus import Resource, marshal_with
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.controllers.parsers.OfferControllerParsers import offerControllerParsers
from app.controllers.documentationModels.OfferControllerDocumentationModels import offerModel
from app.models.Offer import Offer

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class CreateOfferController(Resource):

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
        return Offer.findOfferById(id).serialize(), 200

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class UserOfferController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    def get(self):
        userId = get_jwt_identity()

@offerControllerNamespace.response(400, 'Validation error', error_model)
@offerControllerNamespace.response(500, 'Server error', error_model)
class BookingOfferController(Resource):

    @jwt_required
    @offerControllerNamespace.doc(security='apikey')
    def patch(self, id):
        userId = get_jwt_identity()