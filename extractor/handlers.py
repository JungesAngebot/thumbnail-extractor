from flask import render_template, request

from extractor import frontend
from extractor.controller import AnalysisController
from extractor.system_utils import clean_env


""" Handlers for processing incoming requests. """


@frontend.route('/')
def show_index_page():
    """ Hook to begin video file processing.

    First of all the static/images/ folder is cleaned, what means that all images in their
    will be removed.
    """
    no_gen = True
    if 'nogen' not in request.args:
        no_gen = False
        clean_env()
    images = AnalysisController.analyze_video(no_gen)
    return render_template('index.html', images=images, page='index')


@frontend.route('/thumbnails')
def show_thumbnails():
    """ Hook for displaying all thumbnails generated. """
    images = AnalysisController.get_all_generated_thumbnails()
    return render_template('', images=images, page='overview')
