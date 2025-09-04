from api.models.film_actor import FilmActor
from api.schemas import ma
from marshmallow import EXCLUDE


class FilmActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FilmActor
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

film_actor_schema = FilmActorSchema()
films_actors_schema = FilmActorSchema(many=True)
