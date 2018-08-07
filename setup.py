from setuptools import setup, find_packages

version = '1.0.1'

setup(
  name='ingenix',
  version=version,
  description='Ingenix test',
  author='Aleksei Nikitin',
  packages=find_packages(),
  zip_safe=False,
  include_package_data=True,
  entry_points={
    'console_scripts': [
      'runserver = commands:runserver',
      'runtests = commands:runtests'
    ]
  }
)
