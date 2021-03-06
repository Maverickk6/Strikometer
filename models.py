from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    __tablename__ = "News"
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.Text)
    link = db.Column(db.String, unique=True)
    title = db.Column(db.String)
    time = db.Column(db.DateTime)

    def __repr__(self):
        return "<{} : {}>".format(self.id, self.title)

class Votes(db.Model):
    __table__name = "Votes"
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Boolean)
    downvote = db.Column(db.Boolean)

    def __repr__(self):
        return "<{} : {}>".format(self.id, self.upvote, self.downvote)
