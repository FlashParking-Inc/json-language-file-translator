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

        # get existing translation file, if it exists
        existing_dictionary = {}
        if os.path.exists(target_translation_file_location):
            with open(target_translation_file_location) as target_translation_file:
                existing_dictionary = json.load(target_translation_file)

        # open english file
        with open(english_translation_file_location) as english_translation_file:
            english_dictionary = json.load(english_translation_file)

            # get finished translated dictionary
            translated_dictionary = translate_dictionary(english_dictionary, target_language, filename, existing_dictionary)

            # write translated dictionary to json file for target language
            with open(target_translation_file_location, "w+") as target_translation_file:
                json.dump(translated_dictionary, target_translation_file, indent=2)


def translate_dictionary(english_dictionary, target_language, filename, existing_dictionary={}):

    # create translated dict
    translation_count = traverse(english_dictionary, target_language, existing_dictionary)
    print(f"{translation_count} translations for {target_language} for {filename}")
    # the english dict was modified, so use it as the translated dict
    translated_dictionary = english_dictionary

    return translated_dictionary


def traverse(items, target_language, existing_dictionary={}, path=[]):
    translation_count = 0

    for key, item in items.items():
        if type(item) is str:
            translated_text = get_current_translation(key, path, existing_dictionary)
            if not translated_text:
                translated_text = translate(item, target_language)
                translation_count += 1

            items[key] = translated_text
        elif type(item) is dict:
            path.append(key)
            translation_count += traverse(item, target_language, existing_dictionary, path)

    # pop the path stack, were goin' back up
    if len(path) > 0:
        path.pop(len(path)-1)

    return translation_count


def translate(text, target_language):
    # call to Google Translation API
    translation = t.translate(text, source_language="en", target_language=target_language)
    translated_text = translation["translatedText"]
    # translated_text = f"{target_language}: {item}"

    return translated_text


def get_current_translation(key, path=[], existing_dictionary={}):
    translated_text = None
    try:
        current_dictionary = existing_dictionary

        for path_key in path:
            current_dictionary = current_dictionary[path_key]

        translated_text = current_dictionary[key]
    except:
        pass

    return translated_text


if __name__ == '__main__':
    language = sys.argv[1] or "es"
    translate_to_language(language)
