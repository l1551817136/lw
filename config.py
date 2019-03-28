import os
class Config:
    SECRET_KEY = 'flaskMysql'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIT_SENDER = 'Flasky Admin <liwei@honoka.cc>'
    FLASKY_ADMIN = '1551817136@qq.com'
    DEBUG = True 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
         pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_UAERNAME = 'liwei@honoka.cc'
    MAIL_PASSWORD = 'RuoZhiLi12345'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:honoka.cc@222.197.201.131:3306/lw?charset=utf8' 
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:honoka.cc@222.197.201.131:3306/ycq?charset=utf8'
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:honoka.cc@222.197.201.131:3306/CQ?charset=utf8'
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}