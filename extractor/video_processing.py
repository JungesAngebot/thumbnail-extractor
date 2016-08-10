import os

from moviepy.video.io.VideoFileClip import VideoFileClip

from extractor import APP_ROOT


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
