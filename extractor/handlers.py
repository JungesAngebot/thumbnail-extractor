from flask import render_template

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
    clean_env()
    analysis_data = AnalysisController.analyze_video()
    return render_template('index.html', analysis_data=analysis_data)
