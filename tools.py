
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


