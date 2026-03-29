from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"


def translate_to_english(text):
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except:
        return text