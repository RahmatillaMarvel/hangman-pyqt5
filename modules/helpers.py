import requests
from deep_translator import GoogleTranslator
import webbrowser
import turtle



def get_definition(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        definition = definition.split('.')[0] + '.'

        return definition

    except:
        return 'No definition found.'

def translate_text(text, source_lang='english', target_lang='uzbek'):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_text = translator.translate(text)
    return translated_text

def open_ads(url):
    webbrowser.open(url, new=2)

