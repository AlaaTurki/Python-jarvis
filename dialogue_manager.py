import os
from sklearn.metrics.pairwise import pairwise_distances_argmin
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tools import *

class DialogueManager(object):
    def __init__(self):
        print("Loading resources...")

        # Chit-chat part
        self.create_chitchat_bot()

    def create_chitchat_bot(self):
        """Initializes self.chitchat_bot with some conversational model."""

        
        self.chatbot = ChatBot(
            'cloudwalker',
            trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
        )
        self.chatbot.train("chatterbot.corpus.english")
        self.chatbot.train("chatterbot.corpus.convo-bbc.The Flatmates - Episode 1")
       
    def generate_answer(self, question):      

        response = self.chatbot.get_response(question)
        return response