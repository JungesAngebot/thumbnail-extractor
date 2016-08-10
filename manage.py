from flask.ext.script import Manager

from extractor.flask_app import create_app, configure_environment

manager = Manager(create_app)

if __name__ == '__main__':
    configure_environment()
    manager.run()
