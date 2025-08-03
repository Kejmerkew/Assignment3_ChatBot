from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Command(BaseCommand):
    help = 'Chat with the bot in terminal'

    def handle(self, *args, **kwargs):
         # Create a new chatbot instance with SQL storage
        chatbot = ChatBot(
            'TerminalBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///db.sqlite3' # DB to store learned conversations
        )

        # Create a trainer
        trainer = ChatterBotCorpusTrainer(chatbot)
         # Train the bot using English corpus, greetings, conversations
        trainer.train('chatterbot.corpus.english')
        trainer.train('chatterbot.corpus.english.greetings')
        trainer.train('chatterbot.corpus.english.conversations')

        print("Type something to begin... (type 'exit' to quit)")
        # Infinite loop for chatting until user types 'exit'
        while True:
            user_input = input("user: ")
            if user_input.lower() == 'exit':
                break
            # Get response from chatbot
            response = chatbot.get_response(user_input)
            print(f"bot: {response}")
