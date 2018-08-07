import unittest
from multiprocessing import Process
from api.app import create_app


def runserver():
  app = create_app()
  app.config.from_object('config.testing')
  app.run(use_reloader=False)


def runtests():
  server = Process(target=runserver)
  server.start()
  try:
    suite = unittest.TestLoader().discover('tests.v1', pattern='test_*.py')
    unittest.TextTestRunner().run(suite)
  finally:
    server.terminate()


if __name__ == '__main__':
  runtests()
