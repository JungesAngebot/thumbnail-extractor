import glob
import os

from extractor import APP_ROOT
from extractor.data import Video

""" Commons utils to work with the system. """


def clean_env(audio=True, images=True):
    """ Cleans the static/images folder. """
    if images:
        files = glob.glob('%s/static/images/*' % APP_ROOT)
        for f in files:
            os.remove(f)
    if audio:
        files = glob.glob('%s/static/audios/*' % APP_ROOT)
        for f in files:
            os.remove(f)


def get_all_thumbnails():
    """ Function to get all images prev. generated from a video. """
    files = glob.glob('%s/static/images/*' % APP_ROOT)
    images = []
    for file in files:
        images.append(file.replace('%s/static/images/' % APP_ROOT, ''))
    return images


def get_all_videos():
    """ Gets all videos in the static dir. """
    files = glob.glob('%s/static/videos/*' % APP_ROOT)
    videos = []
    for file in files:
        videos.append(Video.create_from_filename(file))
    return videos
