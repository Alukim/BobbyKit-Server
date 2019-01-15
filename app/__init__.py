import logging
from flask import Flask, Blueprint
from flask_restplus import Api
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError, CSRFError, InvalidHeaderError, JWTDecodeError, WrongTokenError, RevokedTokenError, FreshTokenRequired

__author__ = 'Marcin Gurbiel | Bartosz Kowalski'

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

app = Flask(__name__)
app.logger.setLevel(logging.NOTSET)
blueprint = Blueprint('BobbyKit API', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', version='1.0', title='BobbyKit API documentation', description='API documentation of BobbyKit project', authorizations = authorizations)

app.register_blueprint(blueprint)

app.config.from_object(Config)

jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

from app.models.FileContents import FileContent
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

def RegisterExceptionHandlers():
    @api.errorhandler(NoAuthorizationError)
    def handle_auth_error(e):
        return {'message': str(e)}, 401

    @api.errorhandler(CSRFError)
    def handle_auth_error(e):
        return {'message': str(e)}, 401


    @api.errorhandler(InvalidHeaderError)
    def handle_invalid_header_error(e):
        return {'message': str(e)}, 422


    @api.errorhandler(JWTDecodeError)
    def handle_jwt_decode_error(e):
        return {'message': str(e)}, 422


    @api.errorhandler(WrongTokenError)
    def handle_wrong_token_error(e):
        return {'message': str(e)}, 422


    @api.errorhandler(RevokedTokenError)
    def handle_revoked_token_error(e):
        return {'message': 'Token has been revoked'}, 401


    @api.errorhandler(FreshTokenRequired)
    def handle_fresh_token_required(e):
        return {'message': 'Fresh token required'}, 401

    # @api.errorhandler(DecodeError)
    # def handle_decode_error(e):
    #     return {'message': 'Invalid token'}, 422

RegisterExceptionHandlers()

from app.controllers.AccountController import (
    ns as ns1,
    AccountsLoginController, AccountsLogoutController, AccountsRegisterController)

api.add_namespace(ns1)

ns1.add_resource(AccountsLoginController, '/login')
ns1.add_resource(AccountsLogoutController, '/logout')
ns1.add_resource(AccountsRegisterController, '/register')

from app.controllers.ImageController import (
    ns as ns2,
    UploadImageController, GetImageController)

api.add_namespace(ns2)
ns2.add_resource(UploadImageController, '')
ns2.add_resource(GetImageController, '/<id>')

if __name__ == '__main__':
    app.run(debug=True)