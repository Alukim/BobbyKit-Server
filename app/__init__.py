from flask import Flask
from flask_restplus import Api
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

api = Api(app, version='1.0', title='BobbyKit API', description='A simple API for BobbyKit')


app.config.from_object(Config)



db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import routes
from app.models import models