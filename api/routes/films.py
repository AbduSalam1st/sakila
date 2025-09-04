from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.film import Film
from api.schemas.film import films_schema, film_schema


films_router = Blueprint("film", __name__, url_prefix="/film")

@films_router.get("/")
def read_all_films():
    films = Film.query.all()
    return jsonify(films_schema.dump(films)), 200

@films_router.get('/<film_id>')
def read_film(film_id):
    film = Film.query.get(film_id)
    return film_schema.dump(film)


@films_router.post("/")
def create_film():
    film_data = request.json
    try:
        film_schema.load(film_data)
    except ValidationError as err:
        return jsonify(err), 400

    try:
        film = Film(**film_data)
        db.session.add(film)
        db.session.commit()
    except ValidationError as err:
        return jsonify(err), 400

    return film_schema.dump(film), 201

@films_router.delete('/<film_id>')
def delete_film(film_id):
    film = Film.query.get(film_id)
    db.session.delete(film)
    db.session.commit()

    return films_schema.dump(Film.query.all()), 200

@films_router.patch("/<int:film_id>")
def update_film(film_id):
    data = request.get_json() or {}
    film = Film.query.get_or_404(film_id)
    try:
        film = film_schema.load(data, instance=film, partial=True)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    db.session.commit()
    return film_schema.dump(film), 200
