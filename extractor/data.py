import os

from moviepy.video.io.VideoFileClip import VideoFileClip


class Video(object):
    def __init__(self, clip):
        self.clip = clip

    @classmethod
    def create_from_video_filename(cls, video_filename):
        if not os.path.isfile(video_filename):
            raise FileNotFoundError('No such file %s found!' % video_filename)
        clip = VideoFileClip(video_filename)
        return cls(clip)

