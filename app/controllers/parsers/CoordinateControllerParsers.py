from flask_restplus import Resource, reqparse, fields, marshal_with

class CoordinateControllerParsers():

    getDistanceParser = reqparse.RequestParser(bundle_errors=True)
    getDistanceParser.add_argument('firstLatitude', help = "First latitude of coordinates are required", type = float, required = True, location = 'args')
    getDistanceParser.add_argument('firstLongitude', help = "First longitude of coordinates are required", type = float, required = True, location = 'args')
    getDistanceParser.add_argument('secondLatitude', help = "Second latitude of coordinates are required", type = float, required = True, location = 'args')
    getDistanceParser.add_argument('secondLongitude', help = "Second longitude of coordinates are required", type = float, required = True, location = 'args')