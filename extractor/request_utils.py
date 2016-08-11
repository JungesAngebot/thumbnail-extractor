from flask import request


def is_post_request():
    """ Checks if the current request is a post request. """
    return request.method == 'POST'
