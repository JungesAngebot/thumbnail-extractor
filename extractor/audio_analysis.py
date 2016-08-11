import os


def extract_audio_from_video(video_name):
    """ Extracts audio from a video clip. """
    command = 'ffmpeg -i %s %s/static/audios/out.mp3' % video_name
    os.system(command)
    return 'out.mp3'
