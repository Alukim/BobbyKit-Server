from app import coordinateControllerNamespace
from app.controllers.documentationModels.CoordinateControllerDocumentationModels import distanceResponseModel
from app.controllers.parsers.CoordinateControllerParsers import CoordinateControllerParsers
from app.controllers.responses.DistanceResponse import DistanceResponse
from flask_restplus import Resource, marshal_with
from geopy import distance

class CoordinateController(Resource):

    @coordinateControllerNamespace.marshal_with(distanceResponseModel)
    @coordinateControllerNamespace.doc(parser=CoordinateControllerParsers.getDistanceParser)
    def get(self):

        data = CoordinateControllerParsers.getDistanceParser.parse_args()

        coords_1 = (data.firstLatitude, data.firstLongitude)
        coords_2 = (data.secondLatitude, data.secondLongitude)

        distanceInKm = distance.distance(coords_1, coords_2).km

        return distanceResponse.serialize(distanceInKm), 200
