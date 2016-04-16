from flask import Flask
from egi.config import populate_flask_config

app = Flask(__name__)
populate_flask_config(app)


# This makes me queasy just looking at it, but it's considered the way to go
# for large Flask apps.
# http://flask.pocoo.org/docs/0.10/patterns/packages/#simple-packages
from egi import views  # noqa
from egi import api_resources  # noqa
from egi import errorhandlers  # noqa
