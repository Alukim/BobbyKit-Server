from app import imageControllerNamespace
from app.models.FileContents import FileContent
from app.controllers.documentationModels.ImageControllerDocumentationModels import uploadImageResponseModel
from app.controllers.parsers.ImageControllerParsers import fileParser
from app.controllers.responses.ErrorResponses import errorMessage
from app.controllers.responses.ImageResponseModels import imageResponseModels
from flask_restplus import Resource, marshal_with
from flask import abort, request, make_response

class UploadImageController(Resource):

    @imageControllerNamespace.response(201, 'Image uploaded', uploadImageResponseModel)
    @imageControllerNamespace.expect(fileParser)
    def post(self):
        file = request.files['image']

        if not file:
            return errorMessage.imageNotSend()

        newFile = FileContent(
            name = file.filename,
            data = file.read()
        )

        try:
            newFile.add()
            return imageResponseModels.created(newFile.id)
        except:
            return errorMessage.somethingWentWrong()


class GetImageController(Resource):

    @imageControllerNamespace.doc(model=[str])
    def get(self, id):
        image = FileContent.findById(id)

        if not image:
            return errorMessage.imageDoesNotExist(id)

        return imageResponseModels.imageResponse(image)