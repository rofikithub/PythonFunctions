from langdetect import detect  # pip install langdetect


def detect_input_language(text):
    text = detect(text)
    print(text)
    return text


def main():
    detect_input_language("I Love You")


if __name__ == "__main__":
    main()
