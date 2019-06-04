import json
from random import choice


lib = json.load(open('data.json'))  #unpack the json file


def definition(k):
    """Takes in a keyword and outputs a definition"""
    if k in lib:
        return choice(lib[k])


kword = input("Enter your word : ")

result = definition(kword)

print(result)
