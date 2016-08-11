import os
import librosa

from extractor import APP_ROOT


def extract_audio_from_video(video_name):
    """ Extracts audio from a video clip. """
    command = 'ffmpeg -i %s %s/static/audios/out.mp3' % (video_name, APP_ROOT)
    os.system(command)


def get_speed_and_beats_from_audio():
    """ Determines the speed and beats of an audio file. """
    y, sr = librosa.load('%s/static/audios/out.mp3' % APP_ROOT)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    return tempo, beats

