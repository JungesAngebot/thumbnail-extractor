from flask import render_template

from extractor import frontend
from extractor.system_utils import clean_env


@frontend.route('/')
def show_index_page():
    """ Hook to begin video file processing.

    First of all the static/images/ folder is cleaned, what means that all images in their
    will be removed.
    """
    clean_env()
    return render_template('index.html')
