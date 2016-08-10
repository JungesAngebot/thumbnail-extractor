import glob
import os

from flask import render_template

from extractor import frontend, APP_ROOT


def clean_env():
    """ Cleans the static/images folder. """
    files = glob.glob('%s/static/images/*' % APP_ROOT)
    for f in files:
        os.remove(f)


@frontend.route('/')
def show_index_page():
    """ Hook to begin video file processing.

    First of all the static/images/ folder is cleaned, what means that all images in their
    will be removed.
    """
    clean_env()
    return render_template('index.html')
