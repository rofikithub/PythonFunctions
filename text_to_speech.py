import os
import playsound        # pip install --upgrade setuptools wheel  # pip install playsound
from gtts import gTTS   # pip install gTTS


def text_file_playsound(text):
    toSpeak = gTTS(text=text, lang='bn')
    file = "audio.mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
    print(text)


if __name__ == "__main__":
    text_file_playsound("আমি আপনার জন্য কি করতে পারি ..")

