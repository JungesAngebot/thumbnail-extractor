def determine_best(images):
    """ function determines the best thumbnail out of the given list.

    It checks if the image has a successful face detection, joy or surprise likelihood during face detection
    and checks that the dominant color is not to dark or to bright.
    """
    candidate = None
    for image in images:
        is_friendly_image = has_image_joy_likelihook(image) or has_image_surprise_likelihood(image)
        is_candidate = has_image_faces(image) and is_friendly_image and is_dominant_color_normal(image)
        candidate = image if is_candidate else None
    return candidate


def has_image_faces(image):
    pass


def has_image_joy_likelihook(image):
    pass


def has_image_surprise_likelihood(image):
    pass


def is_dominant_color_normal(image):
    pass
