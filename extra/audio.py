import librosa
audio_path = librosa.util.example_audio_file()
# or uncomment the line below and point it at your favorite song:
# audio_path = '/path/to/your/favorite/song.mp3'
y, sr = librosa.load('out.mp3')
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

print(tempo, beats)
