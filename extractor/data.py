""" Simple module for representing data to be rendered. """


class Image(object):
    """ Image model to represent basic information
    about a single image.
    """

    def __init__(self, image_name, static_url_ref):
        """ Initializer takes just the image name to initialize
        a new instance.
        """
        self.image_name = image_name
        self.static_url_ref = static_url_ref

    def image_stream(self):
        return open(self.image_name, 'rb')

    def set_face_detection_result(self, result):
        for landmark in result[0]['landmarks']:
            pass

    @classmethod
    def create_with_image_name(cls, image_name, static_url_ref):
        """ Creates an instance of the image class based on a file name"""
        return cls(image_name, static_url_ref)


class Landmark(object):
    def __init__(self, landmark_type, x, y, z):
        self.landmark_type = landmark_type
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def create_from_dict(cls, landmark_dict):
        return cls(landmark_dict['type'],
                   landmark_dict['position']['x'],
                   landmark_dict['position']['y'],
                   landmark_dict['position']['y'])

