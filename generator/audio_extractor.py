import sys
from moviepy.editor import *

video = VideoFileClip("videoplayback.mp4")
audio = video.audio
audio.write_audiofile("deneme.wav")