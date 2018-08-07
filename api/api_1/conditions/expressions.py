
def contains(a, b):
  try:
    a.index(b)
  except ValueError as e:
    return False
  return True

def not_contains(a, b):
  try:
    a.index(b)
  except ValueError as e:
    return True
  return False

expressions = {
  'contains': contains,
  'not_contains': not_contains,
  'more': lambda a, b: a > b,
  'less': lambda a, b: a < b,
  'equal': lambda a, b: a == b,
  'in': lambda a, b: a in b,
  'not_in': lambda a, b: not a in b,
}
