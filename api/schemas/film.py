from api.models.film import Film
from api.schemas import ma
from marshmallow import EXCLUDE


class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        load_instance = True
        include_fk = True
        unknown = EXCLUDE

film_schema = FilmSchema()
films_schema = FilmSchema(many=True)
