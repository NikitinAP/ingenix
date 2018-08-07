from flask import request
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from werkzeug.datastructures import MultiDict
from werkzeug.exceptions import BadRequest


class Location(object):

  def __init__(self, location):
    self.location = location

  def source(self, request):
    value = getattr(request, self.location, MultiDict())
    if value is not None:
      return value
    return MultiDict()


class RequestParser(object):

  def __init__(self, location, schema):
    self.schema = schema
    self.location = Location(location)

  def parse(self):
    data = self.location.source(request)

    try:
      error = validate(data, self.schema)
    except ValidationError as e:
      msg = getattr(e, 'message')
      path = '-'.join([str(s) for s in list(getattr(e, 'path'))])
      raise BadRequest('{0} - ({1})'.format(msg, path))

    return data
