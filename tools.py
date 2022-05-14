
import re
import pickle
import numpy as np
import csv
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def openchrome():
    import webbrowser
    webbrowser.open("www.google.com")

def search(query):
    import webbrowser
    webbrowser.open("https://google.com/search?q=%s" % query)

def translate(query,len):
    from googletrans import Translator
    translator = Translator()

    result = translator.translate(text=str(query),dest=len)
    return(result.text)