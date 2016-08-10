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
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)
