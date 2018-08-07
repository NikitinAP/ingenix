from .properties import (
    TextContent,
    TextLength,
    CategoryTitle,
  )


class Object(object):
  pass

class Text(Object):

  def __init__(self, txt):
    self.content = TextContent(txt)
    self.length = TextLength(len(txt))


class Category(Object):

  def __init__(self, txt):
    self.title = CategoryTitle('Новости')
