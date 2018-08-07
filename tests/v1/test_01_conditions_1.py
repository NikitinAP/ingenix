import unittest
from tests.v1 import (
    create_client,
  )


data = {
  'article': 'Текст, который необходимо проверить',
  'conditions': {
    'operator': 'and',
    'rules': [
      {
        'object': 'text',
        'property': 'content',
        'expression': 'contains',
        'value': 'Привет',
      },
      {
        'object': 'text',
        'property': 'length',
        'expression': 'more',
        'value': 10,
      },
    ],
    'groups': [
      {
        'operator': 'or',
        'rules': [
          {
            'object': 'category',
            'property': 'title',
            'expression': 'equal',
            'value': 'Новости',
          },
          {
            'object': 'category',
            'property': 'title',
            'expression': 'equal',
            'value': 'Животные',
          }
        ]
      },
      {
        'operator': 'and',
        'rules': [
          {
            'object': 'category',
            'property': 'title',
            'expression': 'in',
            'value': ['Животные', 'Новости'],
          },
        ]
      }
    ]
  }
}

class ConditionsTests(unittest.TestCase):

  def test_S1(self):
    client = create_client()
    resp, http = client.conditions.validate(json=data).result()
    # print('RESPONSE = ', resp['result'])
    self.assertEqual(http.status_code, 200)
