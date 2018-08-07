import os
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file
from config.testing import ROOT


CLIENT_CONFIG_DEFAULTS = {
  'also_return_response': True
}

def create_client(config={}):
  client = SwaggerClient.from_spec(
    load_file(os.path.join(ROOT, 'static/v1/sw.yaml')),
    config=dict(CLIENT_CONFIG_DEFAULTS, **config)
  )
  return client
