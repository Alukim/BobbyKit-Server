from app import app
from app import api
from flask_restplus import Resource

@api.route('/api/accounts')
class AccountsController(Resource):

    @api.route('/login', methods=['POST'])
    def login():
        return {'TEST':, 'TEST'}

    @api.route('/api/accounts/register', methods=['POST'])
    def register():
        return 'registred'

    @api.route('/api/accounts/logout', methods=['POST'])
    def logout():
        return 'Logout'