class userResponseModels:

    @staticmethod
    def userResponse(user):
        return {
            'id': user.id,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'email': user.email,
            'imageId': user.imageId
        }