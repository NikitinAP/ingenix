from flask_babel import gettext


class BaseError(Exception):

  def __init__(self, **kwargs):
    self.params = kwargs

  def gettext(self, txt):
    return gettext(txt, **self.params)


class UnknownOperator(BaseError):

  @property
  def message(self):
    return self.gettext('Unknown operator %(m)s')


class UnknownObject(BaseError):

  @property
  def message(self):
    return self.gettext('Unknown object %(m)s')


class UnknownProperty(BaseError):

  @property
  def message(self):
    return self.gettext('Unknown property %(m)s')


class UnknownExpression(BaseError):

  @property
  def message(self):
    return self.gettext('Unknown expression %(m)s')

class UnavailableExpression(BaseError):

  @property
  def message(self):
    return self.gettext('Unavailable expression %(m)s for %(p)s')
