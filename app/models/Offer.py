from app import db
from datetime import datetime
from app.models.Availability import Availability
from app.models.Parameter import Parameter
from app import app

class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True, nullable = False)
    category = db.Column(db.String, nullable = False)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    pricePerDay = db.Column(db.Float, nullable = False)
    bail = db.Column(db.Float, nullable = False)
    imageId = db.Column(db.Integer, nullable = True)
    createdAt = db.Column(db.DateTime(False), nullable = False)
    city = db.Column(db.String, nullable = False)
    longitude = db.Column(db.Float, nullable = False)
    latitude = db.Column(db.Float, nullable = False)
    availabilityOn = db.Column(db.Integer, nullable = False, default = 0)
    
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates="offers")

    availability = db.relationship("Availability", back_populates = "offer", uselist=False, lazy='joined')
    parameters = db.relationship("Parameter", back_populates = "offer", lazy='joined')

    @classmethod
    def findOfferById(cls, id):
        return cls.query.filter_by(id = id).first()

    @classmethod
    def findOffersByUserId(cls, userId):
        return cls.query.filter_by(userId = userId)

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

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

        if isCreated == True:
            self.availability = Availability(
                userId = None,
                isBooked = False
            )

            self.__createParameters(details.parameters)

            self.dbAdd()
        else:
            self.dbUpdate()

    def bookTool(self, starDate, endDate, userId):
        self.availability.book(userId)

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
        db.session.update(self)
        db.session.commit()

