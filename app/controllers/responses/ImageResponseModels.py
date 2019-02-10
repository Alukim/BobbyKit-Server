from flask import make_response

class imageResponseModels:

    @staticmethod
    def created(id):
        return {
            'message': id
        }, 201

    @staticmethod
    def imageResponse(image):
        response = make_response(image.data)
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
        'Content-Disposition', 'inline', filename=image.name)
        return response