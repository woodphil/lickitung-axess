
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    DATABASE = '/tmp/acodes.db'
    USERNAME = 'root'
    PASSWORD = ''
    SECRET_KEY = 'BenignBehelith'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/acodes.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
