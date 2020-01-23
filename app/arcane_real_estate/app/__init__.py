from flask import Flask, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

db = SQLAlchemy()


# make sqlite enforce FK constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    authorizations = {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            # 'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token",
        }
    }

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="Arcanific API", version="0.1.0", security="Bearer", authorizations=authorizations)

    register_routes(api, app)

    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    jwt = JWTManager(app)

    # with app.app_context():
    #     print(json.dumps(api.__schema__))

    return app
