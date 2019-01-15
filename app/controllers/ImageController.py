from app import api
from app.models.User import User
from app.models.RevokedTokenModel import RevokedTokenModel
from app.models.FileContents import FileContent
from app.controllers.parsers.AccountControllerParsers import AccountControllerParsers
from flask_restplus import Resource, reqparse, fields, marshal_with, Namespace
from flask import jsonify, abort, request, send_file, make_response
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from werkzeug.datastructures import FileStorage

ns = Namespace('image', description='Images endpoints')

class UploadImageController(Resource):

    fileParser = ns.parser()
    fileParser.add_argument('image', location = 'files', type = FileStorage, required = True)

    @ns.expect(fileParser)
    def post(self):
        file = request.files['image']

        if not file:
            ns.abort(404, 'Image not sended.')

        newFile = FileContent(
            name = file.filename,
            data = file.read()
        )

        try:
            newFile.add()
            return {'message': newFile.id}, 201
        except:
            ns.abort(500, 'Something went wrong')


class GetImageController(Resource):

    @ns.doc(model=[str])
    def get(self, id):
        image = FileContent.findById(id)

        if not image:
            return {'message': 'Image with id {} does not exist'.format(id)}, 404

        response = make_response(image.data)
        response.headers.set('Content-Type', 'image/jpeg')
        response.headers.set(
        'Content-Disposition', 'inline', filename=image.name)
        return response

        # return send_file(
        #     io.BytesIO(image.data),
        #     mimetype='image/jpeg',
        #     as_attachment=True,
        #     attachment_filename='%s.jpg' % image.name
        # )