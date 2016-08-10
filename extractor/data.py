

""" Simple module for representing data to be rendered. """


class Image(object):
    """ Image model to represent basic information
    about a single image.
    """
    def __init__(self, image_name):
        """ Initializer takes just the image name to initialize
        a new instance.
        """
        self.image_name = image_name

    @classmethod
    def create_with_image_name(cls, image_name):
        """ Creates an instance of the image class based on a file name"""
        return cls(image_name)
