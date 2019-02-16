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
    bookToolParser.add_argument('bookedFor', help = 'Id is required', required = True, type = int)

    getOffersParser = reqparse.RequestParser()
    getOffersParser.add_argument('category', location = 'args', type = str)
    getOffersParser.add_argument('city', location = 'args', type = str)
    getOffersParser.add_argument('content', location = 'args', type = str)
    getOffersParser.add_argument('maximumPrice', location = 'args', type = float)
    getOffersParser.add_argument('minimumPrice', location = 'args', type = float)
    getOffersParser.add_argument('maximumDistance', location = 'args', type = float)
    getOffersParser.add_argument('longitude', location = 'args', type = float)
    getOffersParser.add_argument('latitude', location = 'args', type = float)

