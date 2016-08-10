from flask import render_template, request

from extractor import frontend


@frontend.route('/')
def show_index_page():
    return render_template('index.html')
