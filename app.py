# app.py
from flask import Flask
from api.config import config
from api.models import db
from api.schemas import ma
from api.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from api.models import film

    app.register_blueprint(routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

