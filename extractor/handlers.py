from flask import render_template, request

from extractor import frontend
from extractor.controller import extract_frames


@frontend.route('/')
def show_index_page():
    generate_thumbnails = request.args['gen'] if 'gen' in request.args else False
    images = extract_frames()
    return render_template('index.html', images=images)
