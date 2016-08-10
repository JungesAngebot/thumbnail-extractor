from flask import render_template

from extractor import frontend
from extractor.controller import extract_frames


@frontend.route('/')
def show_index_page():
    images = extract_frames()
    return render_template('index.html', images=images)
