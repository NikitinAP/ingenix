from flask import (
    jsonify,
  )
from flask_cors import cross_origin
from functools import partial
from werkzeug.exceptions import HTTPException
from api.restful import (
    status,
  )


class Api(object):

  def __init__(self, blueprint):
    self.blueprint = blueprint
    self.blueprint.record(self._deferred_blueprint_init)


  def add_resource(self, resource, *urls, **kwargs):
    ''' Adds a resource to the api.
    '''
    endpoint = kwargs.pop('endpoint', None) or resource.__name__.lower()

    resource.endpoint = endpoint

    resource_func = resource.as_view(endpoint)
    for url in urls:
      self.blueprint.add_url_rule(url, view_func=resource_func)
    return


  def _deferred_blueprint_init(self, setup_state):
    ''' Отложенная инициализация blueprint
    '''
    setup_state.app.handle_exception = partial(self.error_router, setup_state.app.handle_exception)
    setup_state.app.handle_user_exception = partial(self.error_router, setup_state.app.handle_user_exception)


  def error_router(self, original_handler, e):
    try:
      return self.handle_error(e)
    except Exception:
      pass
    return original_handler(e)

  @cross_origin()
  def handle_error(self, e):
    if isinstance(e, HTTPException):
      code = e.code
      message = getattr(e, 'description', status.get_message(code))
      error = e.__class__.__name__
    else:
      import traceback
      traceback.print_exc()
      code = status.INTERNAL_SERVER_ERROR
      message = status.get_message(code)
      error = 'InternalServerError'

    data = {
      'code': code,
      'status': status.get_status(code),
      'result': {
        'error': error,
        'message': message,
      }
    }
    resp = jsonify(data)
    resp.status_code = code
    return resp

