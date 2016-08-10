import glob
import os

from extractor import APP_ROOT

""" Commons utils to work with the system. """


def clean_env():
    """ Cleans the static/images folder. """
    files = glob.glob('%s/static/images/*' % APP_ROOT)
    for f in files:
        os.remove(f)
