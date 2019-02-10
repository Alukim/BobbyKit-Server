class TokenResponseModel:
    
    @staticmethod
    def userLoggedId(email, token):
        return {
                'message': 'Logged in as {}'.format(email),
                'access_token': token,
            }

    @staticmethod
    def userCreated(email, token):
        return {
                'message': 'User {} was created'.format(email),
                'access_token': token,
            }

    @staticmethod
    def userLogout():
        return {
            'message': 'User logout'
        }