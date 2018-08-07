from api.app import create_app


def runserver():
  app = create_app()
  app.config.from_object('config.dev')
  app.run()

if __name__ == '__main__':
  runserver()
