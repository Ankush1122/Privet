class Config:
    SECRET_KEY = "HK1uEXJ3vbWAkdJLf2Zbj0gVcEyuVT3QyYc6"
    TESTING = False
    DATABASE_URL = "postgres://lexrairfbjcbmi:4a48ea3b7b39af6a23217a709403a00da49d7a8c47725efc463dcb1dc73351f6@ec2-3-226-163-72.compute-1.amazonaws.com:5432/d6utmd1tk5ftjc"

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'privetiitj@gmail.com'
    MAIL_PASSWORD = 'nzln grfo tlwo qtpr'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TSL = False
    MAIL_DEFAULT_SENDER = "privetiitj@gmail.com"

    SALT = "HK1uEXJ3vbWAkdJLf2Zbj0gVcEyuVT3QyYc6"


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

    SESSION_COOKIE_SECURE = True

    IMAGE_UPLOADS = "/app/modules/User/static/assets/images/profiles"


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    IMAGE_UPLOADS = "/media/ankush/Data/Projects/ED_PROJECT_2/modules/User/static/assets/images/profiles"
    SESSION_COOKIE_SECURE = False
