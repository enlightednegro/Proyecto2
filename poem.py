#!/usr/bin/python3

import random


opt = str(input("""Escoge entre:
      1. Vogon
      2. Humano
      Otro. Salir
      Opcion: """))
if opt == "1":
    txt = "vogon.txt"
    poemlen = 30
elif opt == "2":
    txt = "poemdb.txt"
    poemlen = 80
else:
    exit()

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
    while word1 not in chain or not chain[word1]:
        word1 = random.choice(list(chain.keys()))
    word2 = random.choice(list(chain[word1]))
    word1 = word2
    poem += ' ' + word2

print(poem)



