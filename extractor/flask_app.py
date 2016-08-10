import os

from flask import Flask

from extractor import APP_ROOT, frontend


""" Configuration module for bootstrapping the application.

This module creates the flask instance and configures the system environment.
"""


def create_app():
    """ Creates and configures the flask instance. """
    app = Flask(__name__, static_folder=APP_ROOT + '/static', static_url_path='/static',
                template_folder=APP_ROOT + '/templates')
    app.register_blueprint(frontend)
    return app


def configure_environment():
    """ Sets the required env variables.

    Eg. the google auth env variable will be set to point to the auth file used for the vision api.
    """
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '%s/config/junges_angebot.json' % APP_ROOT
