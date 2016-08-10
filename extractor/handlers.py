import glob
import os

from flask import render_template

from extractor import frontend, APP_ROOT


def clean_env():
    files = glob.glob('%s/static/images/*' % APP_ROOT)
    for f in files:
        os.remove(f)


@frontend.route('/')
def show_index_page():
    clean_env()
    return render_template('index.html')
