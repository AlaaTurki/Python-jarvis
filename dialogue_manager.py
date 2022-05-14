import os
from sklearn.metrics.pairwise import pairwise_distances_argmin
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tools import *

class DialogueManager(object):
    def __init__(self, paths):
        print("Loading resources...")
        # Intent recognition:
        self.intent_recognizer = unpickle_file(paths['INTENT_RECOGNIZER'])
        self.tfidf_vectorizer = unpickle_file(paths['TFIDF_VECTORIZER'])

        self.ANSWER_TEMPLATE = 'I think its about %s\n This thread might help you: https://stackoverflow.com/questions/%s'

        # Goal-oriented part:
        self.tag_classifier = unpickle_file(paths['TAG_CLASSIFIER'])

        # Chit-chat part
        self.create_chitchat_bot()

    def create_chitchat_bot(self):
        """Initializes self.chitchat_bot with some conversational model."""

        
        self.chatbot = ChatBot(
            'cloudwalker',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        self.chatbot.train("chatterbot.corpus.english")
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train([
            "Hey",
            "Hello. How do you do?",
        ])
        self.chatbot.train([
            "How are you doing?",
            "I am good as always!",
        ])
        self.chatbot.train([
            "What's your hobby?",
            "I love soccer.",
        ])
        self.chatbot.train([
            "What is AI?",
            "Me",
        ])
        self.chatbot.train([
            "What is your name?",
            "umm, you are interested about me! I am Bob",
        ])
        self.chatbot.train([
            "your name?",
            "I am Bob! did you liked it",
        ])
        self.chatbot.train([
            "What's your name",
            "I am Bob! cool no!",
        ])
       
    def generate_answer(self, question):
        """Combines stackoverflow and chitchat parts using intent recognition."""

        # Recognize intent of the question using `intent_recognizer`.
        # Don't forget to prepare question and calculate features for the question.
        
        prepared_question = text_prepare(question)
        features = self.tfidf_vectorizer.transform([prepared_question])
        intent = self.intent_recognizer.predict(features)[0]

        # Chit-chat part:   
        if intent == 'dialogue':
            # Pass question to chitchat_bot to generate a response.       
            response = self.chatbot.get_response(prepared_question)
            return response
        
        # Goal-oriented part:
        else:        
            # Pass features to tag_clasifier to get predictions.
            tag = self.tag_classifier.predict(features)[0]
            
            # Pass prepared_question to thread_ranker to get predictions.
            thread_id = self.thread_ranker.get_best_thread(prepared_question, tag)
           
            return self.ANSWER_TEMPLATE % (tag, thread_id)