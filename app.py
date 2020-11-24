from moviepy.editor import VideoFileClip
import googletrans
from googletrans import Translator
import subprocess


class Clip:
    def __init__(self, path, name="new_file"):
        self.path = path
        self.name = name
        self.audio = None
        self.text = None
        self.subtitle = None
        self.subtitle_translated = None

    def get_file(self):
        self.video = VideoFileClip(self.path)
        self.audio = self.video.audio

    def extract_audio(self):
        self.audio.write_audiofile(f"{self.name}.wav")

    def generate_from_audio(self):

        # self.subtitle = subtitle

        # with open("subtitle_original.srt", "w", encoding="utf-8") as f:
        #     f.write(self.subtitle)
        # return
        pass

    def translate(self, dest="tr"):

        translator = Translator()
        translated = translator.translate(self.subtitle, dest=dest)
        self.subtitle_translated = translated.text

    def read_sub(self, sub_path):
        pass


    def write_sub(self):
        with open("subtitle_translated.srt", "w", encoding="utf-8") as f:
            f.write(self.subtitle)

    def embed_video(self):
        	subprocess.Popen(f"ffmpeg -i {input} -f srt -i {subtitle} -c:a copy -c:v copy -c:s mov_text -metadata:s:s:0 language=eng -movflags +faststart {output}")





first = Clip(r"video\videoplayback.mp4")
first.get_file()
first.extract_audio()
