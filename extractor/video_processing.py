import os

from moviepy.video.io.VideoFileClip import VideoFileClip

from extractor import APP_ROOT


def get_duration_of_video(video_filename):
    """ Returns the duration for the given video file. """
    clip = VideoFileClip(video_filename)
    return int(clip.duration)


def build_ffmpeg_command_to_extract_frame(second, video_filename, counter):
    command_template = 'ffmpeg -i %s -ss 00:00:%s.32 -vframes 1 %s/static/images/out%s.png'

    return command_template % (video_filename, second, APP_ROOT, counter)


def extract_frames_from_video(video_filename):
    if not os.path.isfile(video_filename):
        raise FileNotFoundError('Cannot find file %s.' % video_filename)
    image_names = []
    second = 0
    for i in range(get_duration_of_video(video_filename)):
        os.system(build_ffmpeg_command_to_extract_frame(second, video_filename, i))
    return image_names
