from app import db
from passlib.hash import pbkdf2_sha256 as sha256

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable = False)
    imageId = db.Column(db.Integer, nullable = True)
    firstName = db.Column(db.String(64), index=True, nullable = False)
    lastName = db.Column(db.String(64), index=True, nullable = False)
    email = db.Column(db.String(120), index=True, unique=True, nullable = False)
    password_hash = db.Column(db.String(128), nullable = False)

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findUserByEmail(cls, email):
        return cls.query.filter_by(email = email).first()

    @classmethod
    def findUserById(cls, id):
        return cls.query.filter_by(id = id).first()

    @staticmethod
    def generateHashedPassword(password):
        return sha256.hash(password)

    @staticmethod
    def verifyPassword(password, hash):
        return sha256.verify(password, hash)

    def __repr__(self):
        return '<User {}>'.format(self.username)