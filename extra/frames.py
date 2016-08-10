# ffmpeg -i malte_running.mp4 -ss 00:00:01.32 -vframes 1 out.png
import os
from subprocess import call

os.system('ffmpeg -i ../malte_running.mp4 -ss 00:00:01.32 -vframes 1 out.png')