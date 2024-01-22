# pip install easygoogletranslate

from easygoogletranslate import EasyGoogleTranslate


def translate_languages(text,source,target):
    translator = EasyGoogleTranslate(
        source_language=source,
        target_language=target,
        timeout=10
    )
    result = translator.translate(text)
    print(result)


def main():
    translate_languages('This is an example.', 'en', 'bn')
    translate_languages('এটি একটি উদাহরণ।', 'bn', 'en')


if __name__ == "__main__":
    main()
