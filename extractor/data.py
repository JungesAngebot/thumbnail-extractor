""" Simple module for representing data to be rendered. """


class Image(object):
    """ Image model to represent basic information
    about a single image.
    """

    def __init__(self, image_name, static_url_ref):
        """ Initializer takes just the image name to initialize
        a new instance.
        """
        self.detection_confidence = None
        self.under_exposed_likelihood = None
        self.anger_likelihood = None
        self.blurred_likelihood = None
        self.sorrow_likelihood = None
        self.joy_likelihood = None
        self.surprise_likelihood = None
        self.image_name = image_name
        self.static_url_ref = static_url_ref
        self.landmarks = []

    def image_stream(self):
        return open(self.image_name, 'rb')

    def set_face_detection_result(self, result):
        for landmark in result[0]['landmarks']:
            self.landmarks.append(Landmark.create_from_dict(landmark))
        self._parse_likelihoods(result)
        self.detection_confidence = result[0]['detectionConfidence'] if 'detectionConfidence' in result[
            0] else 'undefined'

    def _parse_likelihoods(self, result):
        self.surprise_likelihood = result[0]['surpriseLikelihood'] if 'surpriseLikelihood' in result[0] else 'undefined'
        self.joy_likelihood = result[0]['joyLikelihood'] if 'joyLikelihood' in result[0] else 'undefined'
        self.sorrow_likelihood = result[0]['sorrowLikelihood'] if 'sorrowLikelihood' in result[0] else 'undefined'
        self.blurred_likelihood = result[0]['blurredLikelihood'] if 'blurredLikelihood' in result[0] else 'undefined'
        self.anger_likelihood = result[0]['angerLikelihood'] if 'angerLikelihood' in result[0] else 'undefined'
        self.under_exposed_likelihood = result[0]['underExposedLikelihood'] if 'underExposedLikelihood' in result[
            0] else 'undefined'

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
