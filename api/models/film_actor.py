from api.models import db


class FilmActor(db.Model):
    actor_id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, primary_key=True)
    last_update = db.Column(db.DateTime, nullable=False)
