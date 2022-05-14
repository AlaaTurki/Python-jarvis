
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

# Paths for all resources for the bot.
RESOURCE_PATH = {
    'INTENT_RECOGNIZER': 'dataset/intent_recognizer.pkl',
    'TAG_CLASSIFIER': 'dataset/tag_classifier.pkl',
    'TFIDF_VECTORIZER': 'dataset/tfidf_vectorizer.pkl',
    'THREAD_EMBEDDINGS_FOLDER': 'dataset/thread_embeddings_by_tags',
    'WORD_EMBEDDINGS': 'dataset/starspace_embedding.tsv'}


def text_prepare(text):
    """Performs tokenization and simple preprocessing."""
    
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()


def load_embeddings(embeddings_path):
    """Loads pre-trained word embeddings from tsv file.
    Args:
      embeddings_path - path to the embeddings file.
    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """

    embeddings = {}
    with open(embeddings_path, newline='') as embedding_file:
        reader = csv.reader(embedding_file, delimiter='\t')
        for line in reader:
            word = line[0]
            embedding = np.array(line[1:]).astype(np.float32)
            embeddings[word] = embedding
        dim = len(line) - 1
    return embeddings, dim


def question_to_vec(question, embeddings, dim):
    """Transforms a string to an embedding by averaging word embeddings."""

    words_embedding = [embeddings[word] for word in question.split() if word in embeddings]
    # replace embedding with zeros if the embedding is not available
    if not words_embedding:
        return np.zeros(dim)
    words_embedding = np.array(words_embedding)
    return words_embedding.mean(axis=0)


def unpickle_file(filename):
    """Returns the result of unpickling the file content."""
    with open(filename, 'rb') as f:
        return pickle.load(f)