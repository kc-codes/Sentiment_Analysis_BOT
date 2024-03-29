# -*- coding: utf-8 -*-
"""Sentiment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rWqZ5lD-obn1HMR7nIg5yRFHpf6zI5v3
"""

# pip install transformers
# pip install torch
# pip install textblob
# pip install nltk

import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hi there", "Hello, how can I help you today?"]
    ],
    [
        r"what is your name ?",
        ["My name is Mental Health Bot, but you can call me MH Bot for short."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you for asking. How about you?", "I'm a machine learning model, so I don't have feelings as humans do. But I'm always here to help you."]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no worries", "No problem at all."]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear! How can I help you today?"]
    ],
    [
        r"i am (.*)",
        ["That's interesting. Tell me more about yourself."]
    ],
    [
        r"can you help me (.*)",
        ["Of course! I'll do my best to assist you with whatever you need."]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome! I'm always here to help.", "No problem at all. It's what I'm here for."]
    ],
    [
        r"quit",
        ["Goodbye for now. Take care!"]
    ]
]
chatbot = Chat(pairs, reflections)

from textblob import TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score < -0.5:
        return "very negative"
    elif sentiment_score < 0:
        return "negative"
    elif sentiment_score == 0:
        return "neutral"
    elif sentiment_score <= 0.5:
        return "positive"
    else:
        return "very positive"

def get_response(input_text):
    sentiment = get_sentiment(input_text)
    if sentiment == "very negative":
        return "I'm sorry to hear that. I would suggest you call on +91 9619121679 and consult our mental health professional"
    elif sentiment == "negative":
        return "I'm sorry that you're feeling down. How can I help you feel better?"
    elif sentiment == "neutral":
        return "I'm here to listen. Is there anything you'd like to talk about?"
    elif sentiment == "positive":
        return "That's great to hear! Is there anything specific you'd like to discuss?"
    elif sentiment == "very positive":
        return "I'm glad to hear that you're doing well! Is there anything you'd like to talk about?"

def chat():
    print("Hi, I'm MindFlow Bot. How can I help you today?")
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'quit':
                print(chatbot.respond(user_input))
                break
            else:
                response = get_response(user_input)
                sentiment = get_sentiment(response)
                print(response)
                print(f"Sentiment: {sentiment}")
        except Exception as e:
            print("Error: ", str(e))

chat()

