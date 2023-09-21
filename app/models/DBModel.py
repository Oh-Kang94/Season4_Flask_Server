from ..config.Config import db


class User(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(50), primary_key=True)
    refreshtoken = db.Column(db.String(200), nullable=True)  # refreshtoken을 nullable로 설정
    password = db.Column(db.String(45))
    name = db.Column(db.String(45))
    nickname = db.Column(db.String(45))
    address = db.Column(db.String(45))
    insertdate = db.Column(db.String(45))
    deletedate = db.Column(db.String(45), nullable=True)  # deletedate를 nullable로 설정

class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    ott = db.Column(db.String(45))
    title = db.Column(db.String(45))
    imagepath = db.Column(db.String(45))
    releasedate = db.Column(db.String(45))
    genre = db.Column(db.String(45))
    totalaudience = db.Column(db.Integer)
    country = db.Column(db.String(45))
    rating = db.Column(db.String(45))
    star = db.Column(db.Float)
    runningtime = db.Column(db.Integer)
    summary = db.Column(db.Text)

class Review(db.Model):
    __tablename__ = "review"
    user_email = db.Column(db.String(50), db.ForeignKey('user.email'), primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), primary_key=True)
    content = db.Column(db.Text)
    rating = db.Column(db.Float)
    insertdate = db.Column(db.String(45))
    deletedate = db.Column(db.String(45), nullable=True)

    # Define relationships
    user = db.relationship('User', backref='reviews')
    movie = db.relationship('Movie', backref='reviews')

