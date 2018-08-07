
######################################################################
# cors

from flask_cors import CORS


######################################################################
# babel

from flask import request
from flask_babel import Babel

babel = Babel()

@babel.localeselector
def get_locale():
  lang = request.args.get('lang', 'ru')
  return lang
