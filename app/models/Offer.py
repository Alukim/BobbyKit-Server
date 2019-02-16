from app import db
from datetime import datetime
from app.models.Availability import Availability
from app.models.Parameter import Parameter
from app import app

class Offer(db.Model):
    __tablename__ = 'offers'
    __searchable__ = ['category', 'name', 'description']

    id = db.Column(db.Integer, primary_key=True, nullable = False)
    category = db.Column(db.Text, nullable = False)
    name = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    pricePerDay = db.Column(db.Float, nullable = False)
    bail = db.Column(db.Float, nullable = False)
    imageId = db.Column(db.Integer, nullable = True)
    createdAt = db.Column(db.DateTime(False), nullable = False)
    city = db.Column(db.String, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    latitude = db.Column(db.Float, nullable = False)
    availabilityOn = db.Column(db.Integer, nullable = False, default = 0)
    
    searchName = db.Column(db.Text, nullable = False)
    searchDescription = db.Column(db.Text, nullable = False)

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="offers")

    availability = db.relationship("Availability", back_populates = "offer", uselist=False, lazy='joined')
    parameters = db.relationship("Parameter", back_populates = "offer", lazy='joined')

    @classmethod
    def findOfferById(cls, id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findOffersByUserId(cls, userId):
        return cls.query.filter_by(userId = userId).all()

    @classmethod
    def getOffersWithPredicates(cls, query):
        queries = cls.query

        if query.city:
            queries = queries.filter(Offer.city == query.city)

        if query.category:
            queries = queries.filter(Offer.category == query.category)

        if query.minimumPrice:
            queries = queries.filter((Offer.pricePerDay > query.minimumPrice) | (Offer.pricePerDay == query.minimumPrice))

        if query.maximumPrice:
            queries = queries.filter((Offer.pricePerDay < query.maximumPrice) | (Offer.pricePerDay == query.maximumPrice))

        if query.content:
            splittedContent = query.content.split(' ')
            for sc in splittedContent:
                sc = sc.lower()
                queries = queries.filter((Offer.searchDescription.contains(sc)) | (Offer.searchName.contains(sc)))

        return queries.all()

    def create(self, details):
        self.__updateOffer(details, True)

    def update(self, details):
        self.__updateOffer(details, False)

    def __updateOffer(self, details, isCreated):
        self.category = details.category
        self.name = details.name
        self.description = details.description
        self.pricePerDay = details.pricePerDay
        self.bail = details.bail
        self.imageId = details.imageId
        self.createdAt = datetime.now()
        self.city = details.city
        self.longitude = details.longitude
        self.latitude = details.latitude
        self.availabilityOn = details.availabilityOn

        self.searchDescription = details.description.lower()
        self.searchName = details.name.lower()

        if isCreated == True:
            self.availability = Availability(
                userId = None,
                isBooked = False
            )

            self.__createParameters(details.parameters)

            self.dbAdd()
        else:
            self.dbUpdate()

    def bookTool(self, userId, bookedFor):
        self.availability.book(userId, bookedFor)

    def __createParameters(self, params):
        self.parameters = list()
        for par in params:
            param = Parameter(
                key = par['key'],
                value = par['value']
            )
            self.parameters.append(param)
    
    def dbAdd(self):
        db.session.add(self)
        db.session.commit()

    def dbUpdate(self):
        db.session.commit()
