from werkzeug.exceptions import BadRequest
from api.restful import (
    Resource,
    RequestParser,
    status,
  )
from .article import Article
from .errors import BaseError


schema = {
  'type' : 'object',
  'properties' : {
    'article' : { 'type' : 'string' },
    'conditions': { '$ref': '#/definitions/condition' }
  },
  'required': [ 'article', 'conditions' ],
  'additionalProperties': False,
  'definitions': {
    'condition': {
        'type': 'object',
        'properties': {
          'operator': { 'type': 'string' },
          'rules': { 'type': 'array', 'minItems': 1, 'items': { 'type' : 'object', '$ref': '#/definitions/rule' } },
          'groups': { 'type': 'array', 'minItems': 1, 'items': { 'type' : 'object', '$ref': '#/definitions/condition' } }
        },
        'required': [ 'operator' ],
        'minProperties': 2,
        'additionalProperties': False
    },
    'rule': {
      'type': 'object',
      'properties': {
        'object': { 'type': 'string' },
        'property': { 'type': 'string' },
        'expression': { 'type': 'string' },
        'value': {
          'anyOf': [
            { 'type': 'string' },
            { 'type': 'number' },
            { 'type': 'array', 'items': { 'type': 'string' } },
            { 'type': 'array', 'items': { 'type': 'number' } }
          ]
        }
      },
      'required': [ 'object', 'property', 'expression', 'value' ],
      'additionalProperties': False
    }
  }
}

req_parser = RequestParser('json', schema)


class Conditions(Resource):

  def post(self):

    data = req_parser.parse()

    article = data['article']
    conditions = data['conditions']

    a = Article(article)

    try:
      response = a.validate(conditions)
    except BaseError as e:
      raise BadRequest(e.message)

    return response, status.OK
