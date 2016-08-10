import os

from moviepy.video.io.VideoFileClip import VideoFileClip


def get_duration_of_video(video_filename):
    clip = VideoFileClip(video_filename)
    return int(clip.duration)


def extract_frames_from_video(video_filename):
    if not os.path.isfile(video_filename):
        raise FileNotFoundError('Cannot find file %s.' % video_filename)
