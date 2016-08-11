from flask import render_template, request

from extractor import frontend
from extractor.controller import AnalysisController
from extractor.request_utils import is_post_request
from extractor.system_utils import get_all_videos

""" Handlers for processing incoming requests. """


@frontend.route('/', methods=['GET', 'POST'])
def show_index_page():
    """ Hook to begin video file processing.

    First of all the static/images/ folder is cleaned, what means that all images in their
    will be removed.
    """
    if is_post_request():
        video_name = request.form['video']
        audio_analysis = bool(request.form['audio_analysis']) if 'audio_analysis' in request.form else False
        frame_analysis = bool(request.form['frame_analysis']) if 'frame_analysis' in request.form else False
        if audio_analysis:
            pass
        elif frame_analysis:
            AnalysisController.generate_frames(video_name)
    videos = get_all_videos()
    return render_template('index.html', videos=videos, page='index')


@frontend.route('/thumbnails')
def show_thumbnails():
    """ Hook for displaying all thumbnails generated. """
    images = AnalysisController.get_all_generated_thumbnails()
    return render_template('overview.html', images=images, page='overview')


@frontend.route('/thumbnails/<string:image_name>')
def show_single_thumbnail_by_name(image_name):
    """ Hook for displaying a single thumbnail.

    The thumbnail and all detail information will be shown on a single page.
    """
    image = AnalysisController.determine_image_details(image_name)
    return render_template('detail.html', image=image)
