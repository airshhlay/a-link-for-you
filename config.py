import os
import uuid

basedir = os.path.abspath(os.path.dirname(__file__)) # main directory of the application

# set configuration from environment variables, and provide a fallback value when env does not define the variable.
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or uuid.uuid4().hex
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

