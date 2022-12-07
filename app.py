from flask import Flask
from src.base.FlaskAppWrapper import FlaskAppWrapper
from src.routes.HomeRouter import HomeRouter

flask_app = Flask(__name__)
app = FlaskAppWrapper(flask_app)

home_route = HomeRouter("/", "Home")
app.add_endpoint(**home_route)