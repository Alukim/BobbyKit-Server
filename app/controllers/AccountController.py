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
from app.controllers.exceptions.ValidationException import ValidationException
from validate_email import validate_email
import re

@accountControllerNamespace.response(404, 'User not found', error_model)
@accountControllerNamespace.response(400, 'Validation error', error_model)
class AccountsLoginController(Resource):

    @accountControllerNamespace.marshal_with(token_model)
    @accountControllerNamespace.expect(userLoginModel)
    def post(self):
        data = AccountControllerParsers.userLoginParser.parse_args()

        if not validate_email(data.email):
            raise ValidationException('{} is not a valid email'.format(data.email), 'email')

        currentUser = User.findUserByEmail(data.email)

        if not currentUser:
            return errorMessage.userDoesNotExist(data.email), 404
        
        if User.verifyPassword(data.password, currentUser.password_hash):
            accessToken = create_access_token(identity = currentUser.id)
            return TokenResponseModel.userLoggedId(currentUser.email, accessToken), 200
        else:
            return errorMessage.wrongCredential(), 400

@accountControllerNamespace.response(400, 'Validation error', error_model)
@accountControllerNamespace.response(500, 'Server error', error_model)
class AccountsRegisterController(Resource):

    @accountControllerNamespace.marshal_with(token_model, 201)
    @accountControllerNamespace.expect(userRegistrationModel)
    def post(self):
        data = AccountControllerParsers.userRegisterParser.parse_args()
        userDetails = AccountControllerParsers.userDetailsParser.parse_args(req=data)

        if not validate_email(userDetails.email):
            raise ValidationException('{} is not a valid email'.format(userDetails.email), 'details.email')

        if len(data.password) < 5 : 
            raise ValidationException('Minimum length of password is 5', 'password')

        if not re.search("[A-Z]", data.password) : 
            raise ValidationException('Password must have one uppercase letter', 'password')

        if not re.search("[a-z]", data.password) : 
            raise ValidationException('Password must have one lowercase letter', 'password')

        if not re.search("[0-9]", data.password) : 
            raise ValidationException('Password must have one number', 'password')

        if not re.search("[^a-zA-Z0-9]", data.password) : 
            raise ValidationException('Password must have one special character', 'password')

        if data.password != data.confirmPassword :
            return errorMessage.invalidPasswordAndConfirmationPassword(), 400

        currentUser = User.findUserByEmail(userDetails.email)

        if currentUser :
            return errorMessage.userAlreadyExist(userDetails.email), 400

        newUser = User(
            imageId = userDetails.imageId,
            firstName = userDetails.firstName,
            lastName = userDetails.lastName,
            email = userDetails.email,
            password_hash = User.generateHashedPassword(data.password)
        )

        try:
            newUser.saveToDb()
            access_token = create_access_token(identity = newUser.id)
            return TokenResponseModel.userCreated(newUser.email, access_token), 201
        except:
            return errorMessage.somethingWentWrong(), 500

class AccountsLogoutController(Resource):

    @jwt_required
    @accountControllerNamespace.doc(security='apikey')
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return TokenResponseModel.userLogout(), 200
        except:
            return errorMessage.somethingWentWrong(), 500

@accountControllerNamespace.response(401, 'Unauthorized', error_model)
@accountControllerNamespace.response(500, 'Server error', error_model)
class AccountsController(Resource):

    @jwt_required
    @accountControllerNamespace.doc(security='apikey')
    def get(self):
        userId = get_jwt_identity()

        user = User.findUserById(userId)

        return userResponseModels.userResponse(user), 200
