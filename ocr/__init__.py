from flask import Flask

app = Flask(__name__)

from .camera import camera

app.register_blueprint(camera)
