class errorMessage:
    
    @staticmethod
    def somethingWentWrong():
        return {
            'message': 'Something went wrong'
        }

    @staticmethod
    def userDoesNotExist(email):
        return {
            'message': 'User with email: {} does not exists'.format(email)
        }

    @staticmethod
    def userAlreadyExist(email):
        return {
            'message': 'User with email {} already exist'.format(email)
        }

    @staticmethod
    def wrongCredential():
        return {
            'message': 'Wrong credentials'
        }
    
    @staticmethod
    def invalidPasswordAndConfirmationPassword():
        return {
            'message': 'Password and Confirmation password is not equal'
        }

    @staticmethod
    def imageNotSend():
        return  {
            'message': 'Image not send'
        }, 400

    @staticmethod
    def imageDoesNotExist(id):
        return {
            'message': 'Image with id {} does not exist'.format(id)
        }, 404