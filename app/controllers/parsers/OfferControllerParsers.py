from flask_restplus import Resource, reqparse, fields, marshal_with

class offerControllerParsers:

    createUpdateOfferParser = reqparse.RequestParser()
    createUpdateOfferParser.add_argument('offer', help = 'Offer details is required', required = True, type = dict)

    offerDetailsParser = reqparse.RequestParser()
    offerDetailsParser.add_argument('imageId', required = False, type = int, location=('offer',))
    offerDetailsParser.add_argument('category', required = True, type = str, location=('offer',))
    offerDetailsParser.add_argument('name', required = True, type = str, location=('offer',))
    offerDetailsParser.add_argument('pricePerDay', required = True, type = float, location=('offer',))
    offerDetailsParser.add_argument('bail', required = True, type = float, location=('offer',))
    offerDetailsParser.add_argument('description', required = True, type = str, location=('offer',))
    offerDetailsParser.add_argument('parameters', required = False, type = dict, action = 'append', location=('offer',))
    offerDetailsParser.add_argument('city', required = False, type = str, location=('offer',))
    offerDetailsParser.add_argument('longitude', required = False, type = float, location=('offer',))
    offerDetailsParser.add_argument('latitude', required = False, type = float, location=('offer',))
    offerDetailsParser.add_argument('availabilityOn', required = True, type = int, location=('offer',))

    bookToolParser = reqparse.RequestParser()
    bookToolParser.add_argument('id', help = 'Id is required', required = True, type = int)

