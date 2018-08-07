from flask import (
    Flask,
  )
from flask_cors import CORS
from .extensions import (
    babel,
    CORS,
  )


def create_app():
  app = Flask(__name__, static_folder=None, static_url_path=None)

  CORS(app, resources={'*': {'origins': '*'}})

  register_extensions(app)
  register_blueprints(app)

  return app

def register_extensions(app):
  # переводчик текста
  babel.init_app(app)
  return

def register_blueprints(app):
  from api.api_1 import api_1_bp
  app.register_blueprint(api_1_bp)
