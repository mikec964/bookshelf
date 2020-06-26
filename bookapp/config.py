import yaml

class Config:
    with open("keys.yaml", 'r') as config_f:
        keys = yaml.safe_load(config_f)
    SECRET_KEY = keys['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = keys['DATABASE_URI']
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = keys['EMAIL_USER']
    # MAIL_PASSWORD = keys['EMAIL_PASS']
