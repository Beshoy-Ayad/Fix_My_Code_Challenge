from flask import Flask
from api.v1.views.index import *
from api.v1 import app_views

app = Flask(__name__)
app.register_blueprint(app_views)