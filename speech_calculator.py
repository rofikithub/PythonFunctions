import speech_recognition as sr

recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source=source)
        print("বলুন...")
        audio = recognizer.listen(source)
    return audio


def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language='bn-BD')
    except sr.UnknownValueError:
        text = 0
        print("দুঃখিত, আমি এটা বুঝতে পারিনি")
    except sr.RequestError as e:
        text = 0
        print("Error; {0}".format(e))
    return text


def process_voice_command(text):
    try:
        int(text)
        text = int(text)
        return text
    except ValueError:
        return 0


def number_array_plus(arr):
    total: int = 0
    for i in arr:
        total = total + i
    print(total)
    return total


def main():
    listData = []
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        num = process_voice_command(text)
        if num > 0:
            listData.append(num)
            print(listData)
            number_array_plus(listData)


if __name__ == "__main__":
    main()
