def determine_best(images):
    """ function determines the best thumbnail out of the given list.

    It checks if the image has a successful face detection, joy or surprise likelihood during face detection.
    """
    candidate = None
    for image in images:
        is_friendly_image = has_image_joy_likelihood(image) or has_image_surprise_likelihood(image)
        is_candidate = has_image_faces(image) and is_friendly_image
        candidate = image if is_candidate else None
    return candidate


def has_image_faces(image):
    return image.landmarks is not None


def has_image_joy_likelihood(image):
    return image.joy_likelihood == 'VERY_LIKELY'


def has_image_surprise_likelihood(image):
    return image.surprise_likelihood == 'VERY_LIKELY'
