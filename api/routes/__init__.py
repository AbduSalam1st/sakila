from flask import Blueprint

from api.routes.actors import actors_router
from api.routes.films import films_router
from api.routes.films_actors import films_actors_router

### Create API route for film router

routes = Blueprint('api', __name__, url_prefix='/api')

routes.register_blueprint(actors_router)
routes.register_blueprint(films_router)
routes.register_blueprint(films_actors_router)
