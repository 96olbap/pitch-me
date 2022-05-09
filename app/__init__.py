from flask import Flask
from config import config_options

# Create app
def create_app(config_name):
    app = Flask(__name__)

    # Creating app configurations
    app.config.from_object(config_options[config_name])

    # Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app