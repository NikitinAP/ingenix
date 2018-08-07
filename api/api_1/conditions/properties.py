from flask_babel import gettext


class Property(object):

  def __init__(self, value):
    self.value = value


class TextContent(Property):

  available_expressions = {
    'contains': lambda v: gettext('Text does not contain %(v)s', v=v),
    'not_contains': lambda v: gettext('Text contains %(v)s', v=v),
  }


class TextLength(Property):

  available_expressions = {
    'more': lambda v: gettext('Text less than %(v)s characters', v=v),
    'less':  lambda v: gettext('Text more than %(v)s characters', v=v),
    'equal': lambda v: gettext('Text length is not %(v)s characters', v=v),
  }


class CategoryTitle(Property):

  available_expressions = {
    'equal': lambda v: gettext('Сategory is not %(v)s', v=v),
    'in': lambda v: gettext('Сategory is not in %(v)s', v=v),
    'not_in': lambda v: gettext('Сategory is in %(v)s', v=v),
  }
