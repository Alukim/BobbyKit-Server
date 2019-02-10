import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bobby.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'BobbyKitSecretKey'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    PROPAGATE_EXCEPTIONS = True
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_MASK_SWAGGER = False
    FLASK_APP = 'bobby.py'