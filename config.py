import os
#base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'default secret key string'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True

  @staticmethod
  def init_app(app):
    pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql://tracy:Test_123@localhost/test'

class TestingConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql://tracy:Test_123@localhost/test'

class ProductionConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'mysql://tracy:Test_123@localhost/test'

config = {
  'development' : DevelopmentConfig,
  'testing' : TestingConfig,
  'production' : ProductionConfig,
  'default' : DevelopmentConfig
}