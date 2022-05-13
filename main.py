import pyttsx3
import speech_recognition   as sr
from decouple               import config
from datetime               import datetime
from random                 import choice
from pprint                 import pprint
from tools                  import *


username = config('username')
jarvis = config('botname')
engine = pyttsx3.init('sapi5')

# Set Voice, Rate & Volume of Speech
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# The main TOS function
def speak(text):
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
    with sr.Microphone() as source:
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
            query = query.replace('translate', '')
            if query == "":
                speak('Please specify the text to be translated')
            else:
                speak("What language would you like to translate to?")
                len = take_user_input().lower()
                speak("Preparing to translate")
                speak(query + " in spanish is " + translate(query,len))