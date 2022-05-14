import pyttsx3
import speech_recognition   as sr
from decouple               import config
from datetime               import datetime
from random                 import choice
from pprint                 import pprint
from tools                  import *

class Bot(object):
    def __init__(self, dialogue_manager):
        self.dialogue_manager = dialogue_manager

    def get_answer(self, question):
        return self.dialogue_manager.generate_answer(question)

class SimpleDialogueManager(object):
    @staticmethod
    def generate_answer(question):
        return "Hello, world!"


username = config('username')
jarvis = config('botname')
engine = pyttsx3.init('sapi5')

# Set Voice, Rate & Volume of Speech
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
dialogue_manager = SimpleDialogueManager()
bot = Bot(dialogue_manager)

# The main TOS function
def speak(text,len="en"):
    if len=="ar":
        """Speaks the text"""
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('voice', voices[0].id)
    if len=="fr":
        """Speaks the text"""
        engine.setProperty('voice', voices[5].id)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('voice', voices[0].id)
    if len=="es":
        """Speaks the text"""
        engine.setProperty('voice', voices[3].id)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('voice', voices[0].id)
    if len=="it":
        """Speaks the text"""
        engine.setProperty('voice', voices[6].id)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('voice', voices[0].id)
    if len=="de":
        """Speaks the text"""
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()
        engine.setProperty('voice', voices[0].id)
    else:
        """Speaks the text"""
        engine.say(text)
        engine.runAndWait()



# Greet the user
def greet_user():
    """Greets the user"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {username}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {username}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {username}")
    speak(f"I am {jarvis}. How may I assist you?")


# Takes Input
def take_user_input():
    """Takes input from user"""
    
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-in')
        if 'exit' in query or 'stop' in query:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night, take care!")
            else:
                speak('Have a good day!')
            exit()
    except Exception:
        speak('I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open chrome' in query:
            speak('Opening Chrome')
            openchrome()

        if 'search for' in query:
            query = query.replace('search for ', '')
            speak("Searching for" + query)
            search(query)

        if 'translate' in query:

            LANGUAGES = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
            'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

            query = query.replace('translate', '').strip()
            if query == "":
                speak('Please specify the text to be translated')
            else:
                speak("What language would you like to translate to?")
                len = take_user_input().lower()
                if len in LANGUAGES:
                    speak("Preparing to translate")
                    speak("{query} in {len} is".format(query=query, len=len, result=translate(query, LANGUAGES.get(len))))
                    speak("{result}".format(query=query, len=len, result=translate(query, LANGUAGES.get(len))),LANGUAGES.get(len))
                else:
                    speak("Sorry, I do not know that language")


        if 'let\'s chat' in query:
            speak('I\'m happy to chat')
            while True:
                query = take_user_input().lower()
                if 'pause chat' in query:
                    speak('I\'m glad we got to chat! Bye')
                    break
                else:
                    speak(bot.get_answer(query))