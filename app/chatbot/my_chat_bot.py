import chatbot.dictionary.res as re
from janome.tokenizer import Tokenizer
import random

def MyChatBot(name, message):
    
    def get_words(text):
        t = Tokenizer()
        words = [token.surface for token in t.tokenize(text)]
        return words
    
    responses = re.response()
    prompt = tuple(get_words(message))
    flag = True
    for word in prompt:
        if word in responses:
            flag = False
            response = random.choice(responses[word])
        elif word in re.bye:
            flag = False
            response = random.choice(re.bye)
        
    if flag:
        response = random.choice(re.no)
        
    response = name + response
    return response