from rest_api.controller import prediction_app
from flask import Flask

def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(prediction_app)

    return flask_app