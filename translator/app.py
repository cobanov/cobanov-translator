import googletrans
from googletrans import Translator

path = "subtitle.srt"
output_path = "translated.srt"

def read_subtitle(path):
    
    with open(path, mode="r") as f:
        content = f.read()
        
    return content


def write_subtitle(content, output_path):
    
    with open(output_path, mode="w", encoding="utf-8") as f:
        f.write(content.text)


def translate(content, dest="tr"):
    
    translator = Translator()
    ceviri = translator.translate(content, dest=dest)

    return ceviri

def main():
    content = read_subtitle(path)
    ceviri = translate(content)
    write_subtitle(ceviri, output_path)


if __name__ == '__main__':
	main()