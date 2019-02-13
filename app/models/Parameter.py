from app import db

class Parameter(db.Model):
    __tablename__ = 'parameters'

    id = db.Column(db.Integer, primary_key=True, nullable = False)
    key = db.Column(db.String, index = True, nullable = False)
    value = db.Column(db.String, index = True, nullable = False)

    offerId = db.Column(db.Integer, db.ForeignKey('offers.id'), unique=True)
    offer = db.relationship("Offer", back_populates="parameters")

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    def update(self, value):
        self.value = value

    def commitSession(self):
        db.session.commit()

