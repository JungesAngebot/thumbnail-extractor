import os

from commonspy.configuration import OverwriteableConfiguration
from flask import Blueprint

APP_ROOT = os.path.dirname(os.path.abspath(__file__)).replace(os.sep + 'extractor', '')

config = OverwriteableConfiguration.create_from_file('%s/config/config.json' % APP_ROOT)

frontend = Blueprint('frontend', __name__)

from extractor.handlers import *
