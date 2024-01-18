import os
import playsound         # pip install playsound
from gtts import gTTS    # pip install gTTS


def json_to_text_file():
    qus = {
        "question": "আপনার নাম কি ?",
        "option_1": "আব্দুর রহিম",
        "option_2": "আব্দুর রাজ্জাক",
        "option_3": "আব্দুর ছাত্তার",
        "option_4": "রফিকুল ইসলাম",
        "answer": "রফিকুল ইসলাম",
        "note": "কারণ নাম টি আমার বাবা মার পছন্দ।",
    }
    text = (
            " প্রশ্ন :          " + qus['question']
            + " ? অপশন ক .  " + qus['option_1']
            + " ।  অপশন খ . " + qus['option_2']
            + " ।  অপশন গ . " + qus['option_3']
            + " ।  অপশন ঘ . " + qus['option_4']
            )
    print(text)
    return text


def text_file_playsound(output):
    toSpeak = gTTS (text=output, lang='bn' )
    file = "audio.mp3"
    toSpeak.save (file)
    playsound.playsound (file, True)
    os.remove(file)
    print ("উত্তর দিন ...")


if __name__ == "__main__":
    text = json_to_text_file()
    text_file_playsound(text)
