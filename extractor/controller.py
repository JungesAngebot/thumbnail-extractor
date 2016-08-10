

""" Basic controller layer for hooking up the analyzis functionality. """
from extractor import APP_ROOT
from extractor.image_analysis import determine_dominant_color_for_images, run_face_detection
from extractor.video_processing import extract_frames_from_video


class AnalysisController(object):
    """ Basically starts the analysis process for a specified video"""

    @staticmethod
    def analyze_video():
        """ Starts the analysis of the given (static) video. """
        video_filename = '%s/static/videos/sample_summer.mp4' % APP_ROOT
        images = extract_frames_from_video(video_filename)
        determine_dominant_color_for_images(images)
        run_face_detection(images)
        return images

