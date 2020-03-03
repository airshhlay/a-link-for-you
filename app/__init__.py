from flask import Flask
from config import Config
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app = Flask(__name__, static_folder="/templates/static")
app.config.from_object(Config)
app.debug = False
toolbar = DebugToolbarExtension(app)

from app import routes