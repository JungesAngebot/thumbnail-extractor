import os

from moviepy.video.io.VideoFileClip import VideoFileClip

from extractor import APP_ROOT


""" Module for basic image processing.

The only tasks of this module is to get some basic information about the given video
like duration and some frames extracted with ffmpeg.
"""


def get_duration_of_video(video_filename):
    """ Returns the duration for the given video file. """
    clip = VideoFileClip(video_filename)
    return int(clip.duration)


def build_ffmpeg_command_to_extract_frame(second, video_filename, counter):
    """ Builds the required ffmpeg command to extract a frame from a video.

    The command to build is used to extract a frame from a video, from the given time.
    The resulting frame will be stored under static/images/out<>.png.
    """
    command_template = 'ffmpeg -i %s -ss 00:00:%s.32 -vframes 1 %s/static/images/out%s.png'

    return command_template % (video_filename, second, APP_ROOT, counter)


def extract_frames_from_video(video_filename):
    """ Extracts frames from the fiven video.

    Only takes the first minute of the video to extract frames from it. Frame
    extraction is done video ffmpeg and the resulting images are stored as png under
    static/images. All resulting images following the naming pattern
    out<NumberOfTheImage>.png. This makes it easier to get the images for further processing.
    """
    if not os.path.isfile(video_filename):
        raise FileNotFoundError('Cannot find file %s.' % video_filename)
    image_names = []
    second = 0
    video_duration = get_duration_of_video(video_filename)
    for i in range(video_duration):
        os.system(build_ffmpeg_command_to_extract_frame(second, video_filename, i))
        if second >= video_duration or second >= 60:
            break
        image_names.append('%s/static/images/out%s.png' % (APP_ROOT, i))
    return image_names
