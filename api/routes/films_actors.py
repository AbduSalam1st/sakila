from flask import Blueprint

from api.models import db
from api.models.actor import Actor
from api.schemas.actor import actors_schema
from api.models.film import Film
from api.schemas.film import films_schema
from api.models.film_actor import FilmActor


films_actors_router = Blueprint("film_actor", __name__, url_prefix="/film_actor")

@films_actors_router.get("/<int:film_id>/actors")
def get_actors_for_film(film_id):
    actor_ids = (
        db.session.query(FilmActor.actor_id)
        .filter(FilmActor.film_id == film_id)
        .all()
    )

    actor_ids = [a[0] for a in actor_ids]

    actors = db.session.query(Actor).filter(Actor.actor_id.in_(actor_ids)).all()
    return actors_schema.dump(actors), 200


@films_actors_router.get("/<int:actor_id>/films")
def get_films_for_actor(actor_id):
    film_ids = (
        db.session.query(FilmActor.film_id)
        .filter(FilmActor.actor_id == actor_id)
        .all()
    )

    film_ids = [a[0] for a in film_ids]

    films = db.session.query(Film).filter(Film.film_id.in_(film_ids)).all()
    return films_schema.dump(films), 200
