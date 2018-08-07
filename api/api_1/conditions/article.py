from collections import defaultdict
from .expressions import expressions
from .operators import operators
from .properties import Property
from .objects import (
    Object,
    Text,
    Category,
  )
from .errors import (
    UnknownOperator,
    UnknownObject,
    UnknownProperty,
    UnknownExpression,
    UnavailableExpression,
  )


class Article(object):

  def __init__(self, value):
    self.value = value

  @property
  def text(self):
    return Text(self.value)

  @property
  def category(self):
    # TODO! Добавить кеширование
    return Category(self.value)


  def validate(self, conditions):

    def _validate(condition):

      res = defaultdict(list)

      # Неизвестный оператор
      if not condition['operator'] in operators:
        raise UnknownOperator(m=condition['operator'])

      if not condition.get('groups') is None:

        for group in condition['groups']:
          res['groups'].append(_validate(group))


      for rule in condition['rules']:
        obj = getattr(self, rule['object'])

        # неизвестный object
        if obj is None or not isinstance(obj, Object):
          raise UnknownObject(m=rule['object'])

        prop = getattr(obj, rule['property'])

        # неизвестный property
        if prop is None or not isinstance(prop, Property):
          raise UnknownProperty(m=rule['property'])

        # неизвестный expression
        if not rule['expression'] in expressions:
          raise UnknownExpression(m=rule['expression'])

        # недоступный expression для данного property
        if not rule['expression'] in prop.available_expressions:
          raise UnavailableExpression(m=rule['expression'], p=rule['property'])

        expression = expressions[rule['expression']]

        is_valid = expression(prop.value, rule['value'])

        (is_valid, error) = (True, '') if is_valid else (False, prop.available_expressions[rule['expression']](rule['value']))

        res['rules'].append({ 'is_valid': is_valid, 'error': error })

        operator = operators[condition['operator']]


      rules_valid = [r['is_valid'] for r in res['rules']]
      groups_valid = [g['is_valid'] for g in res.get('groups', [])]

      res['is_valid'] = operator(rules_valid + groups_valid)

      return res

    return _validate(conditions)


def get_conditions_as_text(conditions):

  def _get_conditions_as_text(condition):

    res = []

    for rule in condition['rules']:

      res.append('{0} {1} {2} {3}'.format(rule['object'], rule['property'], rule['expression'], rule['value']))

    if not condition.get('groups') is None:

      for group in condition['groups']:

        res.append('( {0} )'.format(_get_conditions_as_text(group)))

    return '\n{0}\n'.format(condition['operator'].upper()).join(res)

  return _get_conditions_as_text(conditions)
