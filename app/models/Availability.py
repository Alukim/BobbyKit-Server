from app import db

class Availability(db.Model):
    __tablename__ = 'availabilities'

    id = db.Column(db.Integer, primary_key=True, nullable = False)
    userId = db.Column(db.Integer, index=True, nullable = True)
    isBooked = db.Column(db.Boolean, index=True, nullable = False)
    bookedFor = db.Column(db.Integer, nullable = True)

    offerId = db.Column(db.Integer, db.ForeignKey('offers.id'), unique=True)
    offer = db.relationship("Offer", back_populates = "availability")

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    def book(self, userId):
        self.userId = userId
        self.isBooked = True

    def commitSession(self):
        db.session.commit()

