import os
import uuid

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or uuid.uuid4().hex