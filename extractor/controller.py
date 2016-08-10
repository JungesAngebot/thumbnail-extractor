

""" Basic controller layer for hooking up the analyzis functionality. """
from extractor import APP_ROOT


class AnalysisController(object):
    """ Basically starts the analysis process for a specified video"""

    @staticmethod
    def analyze_video():
        video_filename = '%s/static/videos/sample_summer.mp4' % APP_ROOT

