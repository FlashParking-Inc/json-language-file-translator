from google.cloud import translate_v2
import sys
import os
import json


t = translate_v2.Client()


def translate_to_language(target_language):
    english_directory = "locales/en"
    target_language_directory = os.path.join("locales", target_language)

    # create translation directory if it does not exist
    if not os.path.exists(target_language_directory):
        os.makedirs(target_language_directory)

    # go thru each translation file in english
    for filename in (os.listdir(english_directory)):
        english_translation_file_location = os.path.join(english_directory, filename)
        target_translation_file_location = os.path.join(target_language_directory, filename)
        # open english file
        with open(english_translation_file_location) as english_translation_file:
            english_dictionary = json.load(english_translation_file)

            # get translations
            translated_dictionary = translate_dictionary(english_dictionary, target_language, filename)

            with open(target_translation_file_location, "w+") as target_translation_file:
                json.dump(translated_dictionary, target_translation_file, indent=2)


def translate_dictionary(english_dictionary, target_language, filename):

    translation_count = translate(english_dictionary, target_language)
    translated_dictionary = english_dictionary

    print(f"{translation_count} translations for {target_language} for {filename}")

    return translated_dictionary


def translate(items, target_language):
    translation_count = 0

    for key, item in items.items():
        if type(item) is str:
            # call to Google Translation API
            translation = t.translate(item, source_language="en", target_language=target_language)
            translated_text = translation["translatedText"]
            # translated_text = f"{target_language}: {item}"
            items[key] = translated_text
            translation_count += 1
        elif type(item) is dict:
            translation_count += translate(item, target_language)

    return translation_count


if __name__ == '__main__':
    language = sys.argv[1] or "es"
    translate_to_language(language)
