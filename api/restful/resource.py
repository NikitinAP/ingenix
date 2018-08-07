from flask import (
    jsonify,
  )
from flask.views import MethodView
from functools import wraps
from api.restful import (
    status,
  )


def json_output(function):
  ''' Формирует json-ответ запроса
  '''

  @wraps(function)
  def wrapper(*args, **kwargs):
    data, code = function(*args, **kwargs)
    resp = jsonify(data)
    resp.status_code = code
    return resp

  return wrapper


def format_results(function):
  ''' Прикрепляет мета-поля к ответу запроса
  '''

  @wraps(function)
  def wrapper(*args, **kwargs):
    data, code = function(*args, **kwargs)
    data = {
      'status': status.get_status(code),
      'code': code,
      'result': data,
    }
    return data, code

  return wrapper


class Resource(MethodView):

  decorators = [format_results, json_output]
