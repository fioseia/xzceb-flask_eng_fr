"""
Module to translate from english to french and from french to english
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    authenticator=authenticator,
    version='2018-05-01'
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Function that translates english text to french
    """
    translation = language_translator.translate(text=english_text, model_id='en-fr')
    french_text = translation.get_result()
    return french_text['translations'][0]['translation'].lower()

def french_to_english(french_text):
    """
    Function that translates french text to english
    """
    translation = language_translator.translate(text=french_text, model_id='fr-en')
    english_text = translation.get_result()
    return english_text['translations'][0]['translation'].lower()
