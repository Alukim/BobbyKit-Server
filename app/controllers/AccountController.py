from app import api
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel
from app.controllers.parsers.AccountControllerParsers import AccountControllerParsers
from flask_restplus import Resource, reqparse, fields, marshal_with, Namespace
from flask import jsonify, abort
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

ns = Namespace('accounts', description='Accounts endpoints')

class AccountsLoginController(Resource):

    userLoginModel = ns.model('Login', {'email' : fields.String('User email.'), 'password' : fields.String('User password')})

    @ns.expect(userLoginModel)
    def post(self):
        data = AccountControllerParsers.userLoginParser.parse_args()

        currentUser = User.findUserByEmail(data.email)

        if not currentUser:
            return {'message' : 'User with email: {} does not exists'.format(data.email)}, 404
        
        if User.verifyPassword(data.password, currentUser.password_hash):
            accessToken = create_access_token(identity = currentUser.id)
            return jsonify({
                'message': 'Logged in as {}'.format(currentUser.email),
                'access_token': accessToken,
            })
        else:
            return {'message' : 'Wrong credentials'}, 404

class AccountsRegisterController(Resource):

    userRegistrationDetailsModel = ns.model('User Details model', {
        'imageId': fields.Integer('Id of user image'),
        'firstName' : fields.String('User first name'),
        'lastName' : fields.String('User last name'),
        'email' : fields.String('User email')
    })

    userRegistrationModel = ns.model('Registration model', {
        'password': fields.String("User password"),
        'confirmPassword' : fields.String("Confirmation password"),
        'details' : fields.Nested(userRegistrationDetailsModel)
    })

    @ns.expect(userRegistrationModel)
    def post(self):
        data = AccountControllerParsers.userRegisterParser.parse_args()
        userDetails = AccountControllerParsers.userDetailsParser.parse_args(req=data)

        if data.password != data.confirmPassword :
            return {'message' : 'Password and Confirmation password is not equal'}, 404

        currentUser = User.findUserByEmail(userDetails.email)

        if currentUser :
            return {'message': 'User with email {} already exist'.format(userDetails.email)}, 404

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
            return {
                'message': 'User {} was created'.format(newUser.email),
                'access_token': access_token
                }
        except:
            return {'message': 'Something went wrong'}, 500

class AccountsLogoutController(Resource):

    @jwt_required
    @ns.doc(security='apikey')
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'User logout'}
        except:
            return {'message': 'Something went wrong'}, 500