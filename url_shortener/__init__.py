from flask import Flask

from .extensions import db
from .routes import short

app = Flask(__name__)

app.config.from_pyfile('settings.py')

db.init_app(app)

app.register_blueprint(short)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oadzoiwprhukgt:c3f5331f6c3ab1f84ce76fa5c3222d07f9c6e4465a726d1c4a69fc1759c8fda0@ec2-52-31-233-101.eu-west-1.compute.amazonaws.com:5432/d5kvgr76ueoke1'

#app.config.from_object('config')


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(short)


    return app