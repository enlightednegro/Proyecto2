#!/usr/bin/python3

import random


opt = input("""Escoge entre:
      1. Vogon
      Otro. Humano
      Opcion: """)
if opt == "1":
    txt = "vogon.txt"
    poemlen = 30
else:
    txt = "poemdb1.txt"
    poemlen = 80

with open(txt) as file:
    poemdb = file.read()

poemdb = ''.join([i for i in poemdb if not i.isdigit() ]).replace("\n\n", " ").split(' ')

chain = {}
word_index = 1

for word in poemdb[word_index:]:
    key = poemdb[word_index - 1]
    if key in chain:
        chain[key].append(word)
    else:
        chain[key] = [word]
    word_index += 1


word1 = random.choice(list(chain.keys()))

poem = word1.capitalize()

while poemlen > len(poem.split(' ')):
    word2 = random.choice(list(chain[word1]))
    word1 = word2
    poem += ' ' + word2

print(poem)



