""" Basic controller layer for hooking up the analyzis functionality. """
from extractor import APP_ROOT
from extractor.data import Image
from extractor.image_analysis import determine_dominant_color_for_images, run_face_detection, \
    determine_dominant_color_for_image, detect_face, determine_color_codes_for_image
from extractor.rendering import highlight_faces
from extractor.system_utils import get_all_thumbnails
from extractor.video_processing import extract_frames_from_video


class AnalysisController(object):
    """ Basically starts the analysis process for a specified video"""

    @staticmethod
    def generate_frames(video_filename):
        """ Just invokes frame creation for the given video. """
        extract_frames_from_video('%s/static/videos/%s' % (APP_ROOT, video_filename), False)

    @staticmethod
    def analyze_video(no_gen):
        """ Starts the analysis of the given (static) video. """
        video_filename = '%s/static/videos/sample_summer.mp4' % APP_ROOT
        images = extract_frames_from_video(video_filename, no_gen)
        determine_dominant_color_for_images(images)
        run_face_detection(images)
        return images

    @staticmethod
    def get_all_generated_thumbnails():
        """ Controller hook to get all thumbnails prev. generated. """
        return get_all_thumbnails()

    @staticmethod
    def determine_image_details(image_name):
        """ Analysis the given image and returns an image object with all information. """
        image = Image.create_with_image_name('%s/static/images/%s' % (APP_ROOT, image_name), image_name)
        image.dominant_color = determine_dominant_color_for_image(image)
        result = detect_face(image.image_stream())
        image.set_face_detection_result(result)
        highlight_faces(image.image_name, image.raw_face_detection,
                        '%s/static/images/detection_%s' % (APP_ROOT, image_name))
        image.rendered_with_face_detection_name = 'detection_%s' % image_name
        image.color_palette = determine_color_codes_for_image(image)
        return image
