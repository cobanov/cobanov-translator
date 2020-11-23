import subprocess

INPUT = "videoplayback.mp4"
OUTPUT = "output.mp4"
SUBTITLE = "subtitles.srt"

def embed(input, output, subtitle):
	subprocess.Popen(f"ffmpeg -i {input} -f srt -i {subtitle} -c:a copy -c:v copy -c:s mov_text -metadata:s:s:0 language=eng -movflags +faststart {output}")

def main():
	embed(INPUT, OUTPUT, SUBTITLE)

if __name__ == '__main__':
	main()