import logging
from flask import Flask, Blueprint
from flask_restplus import Api, Namespace
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError, CSRFError, InvalidHeaderError, JWTDecodeError, WrongTokenError, RevokedTokenError, FreshTokenRequired
from flask_marshmallow import Marshmallow
from app.controllers.exceptions.ValidationException import ValidationException

__author__ = 'Marcin Gurbiel | Bartosz Kowalski'

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

app = Flask(__name__)
blueprint = Blueprint('BobbyKit API', __name__, url_prefix='/api')
api = Api(blueprint, doc='/documentation', version='1.0', title='BobbyKit API documentation', description='API documentation of BobbyKit project', authorizations = authorizations)

app.register_blueprint(blueprint)

app.config.from_object(Config)

jwt = JWTManager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

from app.models.FileContents import FileContent
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel
from app.models.Availability import Availability
from app.models.Parameter import Parameter
from app.models.Offer import Offer

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

    @api.errorhandler(ValidationException)
    def handle_validation_exception(e):
        return {
            'message': e.args[0],
            'field': e.field
        }, 400

RegisterExceptionHandlers()

imageControllerNamespace = Namespace('image', description='Images endpoints')
accountControllerNamespace = Namespace('accounts', description='Accounts endpoints')
toolsCategoryControllerNamespace = Namespace('toolCategory', description='Tool category endpoints')
coordinateControllerNamespace = Namespace('coordinate', description='Coordinate endpoints')
offerControllerNamespace = Namespace('offer', description="Offer endpoints")

from app.controllers.AccountController import AccountsLoginController, AccountsLogoutController, AccountsRegisterController, AccountsController
from app.controllers.ImageController import UploadImageController, GetImageController
from app.controllers.ToolsCategoryController import ToolCategoryController
from app.controllers.CoordinateController import CoordinateController
from app.controllers.OfferController import OffersController, OfferController, UserOfferController, BookingOfferController

api.add_namespace(accountControllerNamespace)
api.add_namespace(imageControllerNamespace)
api.add_namespace(toolsCategoryControllerNamespace)
api.add_namespace(coordinateControllerNamespace)
api.add_namespace(offerControllerNamespace)

accountControllerNamespace.add_resource(AccountsLoginController, '/login')
accountControllerNamespace.add_resource(AccountsLogoutController, '/logout')
accountControllerNamespace.add_resource(AccountsRegisterController, '/register')
accountControllerNamespace.add_resource(AccountsController, '')

imageControllerNamespace.add_resource(UploadImageController, '')
imageControllerNamespace.add_resource(GetImageController, '/<int:id>')

toolsCategoryControllerNamespace.add_resource(ToolCategoryController, '')

coordinateControllerNamespace.add_resource(CoordinateController, '/distance')

offerControllerNamespace.add_resource(OffersController, '')
offerControllerNamespace.add_resource(OfferController, '/<int:id>')
offerControllerNamespace.add_resource(UserOfferController, '/user')
offerControllerNamespace.add_resource(BookingOfferController, '/<int:id>/bookTool')

if __name__ == '__main__':
    app.run()