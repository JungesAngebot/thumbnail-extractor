import base64

from colorthief import ColorThief
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

""" This module performs analysis of given images.

Analysis:
- detect dominant color
- detect faces in an image
"""


DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def determine_dominant_color_for_images(images):
    """ Detects the dominant color for each given image.

    To detect the dominant color this function uses color thief.

    :param images: images to detect the dominant color
    :return: nothing (call by reference)
    """
    for image in images:
        color_thief = ColorThief(image.image_name)
        dominant_color = 'nocolor'
        try:
            dominant_color = color_thief.get_color(quality=1)
        except:
            pass
        image.dominant_color = dominant_color


def get_vision_service():
    """ Authenticates to the google vision api.

    If the google authentication env variable is set to a specific service account file
    this will be uses internally by the google cloud sdk. Otherwise this
    code must be run in the google compute env.
    """
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)


def run_face_detection(images):
    """ Runs the face detection with google vision for each
    given image.
    """
    for image in images:
        result = detect_face(image.image_stream())
        image.set_face_detection_result(result)


def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the faces in the picture.
        :param face_file:
        :param max_results:
    """
    image_content = face_file.read()
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('UTF-8')
        },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
        }]
    }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
    })
    response = request.execute()

    return response['responses'][0]['faceAnnotations'] if 'faceAnnotations' in response['responses'][0] else None
