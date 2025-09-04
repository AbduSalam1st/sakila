from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.actor import Actor
from api.schemas.actor import actor_schema, actors_schema

# Create a "Blueprint", or module
# We can insert this into our Flask app
actors_router = Blueprint('actors', __name__, url_prefix='/actors')


# GET requests to the collection return
# a list of all actors in the database
@actors_router.get('/')
def read_all_actors():
    actors = Actor.query.all()               # Get all the actors
    return actors_schema.dump(actors)  # Serialize the actors


# GET requests to a specific document in
# the collection return a single actor
@actors_router.get('/<actor_id>')
def read_actor(actor_id):
    actor = Actor.query.get(actor_id)  # Get the actor by id
    return actor_schema.dump(actor)    # Serialize the actor


@actors_router.post('/')
def create_actor():
    actor_data = request.json          # Get the parsed request body

    try:
        actor_schema.load(actor_data)  # Validate against the schema
    except ValidationError as err:
        return jsonify(err.messages), 400

    actor = Actor(**actor_data)        # Create a new actor model
    db.session.add(actor)              # Insert the record
    db.session.commit()                # Update the database

    return actor_schema.dump(actor)    # Serialize the created actor

@actors_router.put("/<actor_id>")
def put_actor(actor_id):
    data = request.get_json()
    try:
        valid = actor_schema.load(data)            # require both names
    except ValidationError as err:
        return jsonify(err.messages), 400

    actor = Actor.query.get_or_404(actor_id)       # 404 if not found
    actor.first_name = valid["first_name"]
    actor.last_name  = valid["last_name"]
    db.session.commit()
    return actor_schema.dump(actor), 200           # or 204 without

@actors_router.delete("/<actor_id>")
def delete_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)  # 404 if not found
    db.session.delete(actor)                  # delete the instance
    db.session.commit()

    return actors_schema.dump(Actor.query.all()), 200 # Return current table

