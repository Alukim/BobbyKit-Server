from app import db

class FileContent(db.Model):
    __tablename__ = 'FileContents'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id = id).first()
