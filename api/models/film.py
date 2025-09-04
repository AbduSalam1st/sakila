from api.models import db


class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.Integer, db.ForeignKey("language.language_id"),
                            nullable=False, default=1)
    original_language_id = db.Column(db.Integer,
                                     db.ForeignKey
                                     ("language.language_id"),
                                     nullable=True)
    rental_duration = db.Column(db.Integer)
    rental_rate = db.Column(db.Float, nullable=True)
    length = db.Column(db.Integer)
    replacement_cost = db.Column(db.Float, nullable=True)
    rating = db.Column(db.String(10), nullable=True)
    special_features = db.Column(db.String(255), nullable=True)
    last_update = db.Column(db.DateTime, nullable=True)
