from app import app
from app import api
from flask_restplus import Resource

@api.route('/api/accounts')
class AccountsController(Resource):

    @api.route('/api/accounts/login', methods=['POST'])
    def login():
        return "login"

    @api.route('/api/accounts/register', methods=['POST'])
    def register():
        return 'registred'

    @api.route('/api/accounts/logout', methods=['POST'])
    def logout():
        return 'Logout'