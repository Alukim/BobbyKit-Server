from app import accountControllerNamespace
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

class CreateOfferController(Resource):

    def post(self):
        return {}

class OfferController(Resource):

    def patch(self, id):
        return {}

    def get(self, id):
        return {}

class UserOfferController(Resource):

    def get(self):
        return {}

class BookingOfferController(Resource):

    def patch(self, id):
        return id