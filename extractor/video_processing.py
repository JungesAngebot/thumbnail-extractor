import os


def extract_frames_from_video(video_filename):
    if not os.path.isfile(video_filename):
        raise FileNotFoundError('Cannot find file %s.' % video_filename)
