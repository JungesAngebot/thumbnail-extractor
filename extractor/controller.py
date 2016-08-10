import base64
import os

from colorthief import ColorThief
from googleapiclient import discovery
from moviepy.video.io.VideoFileClip import VideoFileClip
from oauth2client.client import GoogleCredentials

from extractor import APP_ROOT
from extractor.kaltura import get_category_metadata_api_string, execute_kaltura_request

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)


def extract_frames():
    second = 0
    image_names = []
    for i in range(18):
        second += 2
        command = 'ffmpeg -i malte_running.mp4 -ss 00:00:%s.32 -vframes 1 %s/static/images/out%s.png' % (
            second, APP_ROOT, i)
        os.system(command)
        if second >= 18:
            break
        image_names.append({
            'name': 'out%s.png' % i,
            'dominant_color': get_dominant_color('out%s.png' % i),
            'metadata': execute_kaltura_request(get_category_metadata_api_string('40293212')),
            'face_detection': detect_face(open('%s/static/images/out%s.png' % (APP_ROOT, i), 'rb'))

        })
    return image_names


def video_info(filename):
    clip = VideoFileClip('%s/static/images/%s' % (APP_ROOT, filename))
    print(clip.duration)
    print(clip.end)
    print(clip.fps)


def get_dominant_color(image_name):
    image_path = '%s/static/images/%s' % (APP_ROOT, image_name)
    color_thief = ColorThief(image_path)
    try:
        dominant_color = color_thief.get_color(quality=1)
    except:
        dominant_color = 'nocolor'
    return dominant_color


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

    return response['responses'][0]['faceAnnotations']
