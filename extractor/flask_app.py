import os

from flask import Flask

from extractor import APP_ROOT, frontend


def create_app():
    app = Flask(__name__, static_folder=APP_ROOT + '/static', static_url_path='/static',
                template_folder=APP_ROOT + '/templates')
    app.register_blueprint(frontend)
    return app


def configure_environment():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '%s/config/junges_angebot.json' % APP_ROOT
