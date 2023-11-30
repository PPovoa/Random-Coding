#===============================
# Avent of Code 2019 - Day 2
#
# Made by: Pedro Póvoa
# Date: 30/06/2020
#===============================

# === CODE ===
import math

fich= open('input.txt', 'r') # open 'input.txt' file

for a in range(100):
    for b in range(100):
        fich.seek(0,0)

        currpointer=0 # current position of the pointer

        text = fich.read().split(',')

        # convert str to int
        for aux in range(0, len(text)):
            text[aux] = int(text[aux])

        # initial changes
        text[1] = a
        text[2] = b

        for i in text: # size of text = 121
            editpos= int(text[currpointer+3]) # position that will suffer changes

            if text[currpointer] == 1: # add the following two in the corresponding position
                text[editpos] = text[text[currpointer+1]]+text[text[currpointer+2]]
                
            elif text[currpointer] == 2: # multiplies the following two in the corresponding position
                text[editpos] = text[text[currpointer+1]]*text[text[currpointer+2]]
            
            elif text[currpointer] == 99: # halt the program
                break

            else:
                print("ERRO - curr:", currpointer, "text:", text[currpointer])
                break

            currpointer += 4 # skip to the instructions

        if text[0] == 19690720:
            print(text)
            print("noun=", a, "verb=", b)
            print("Result:", 100*a+b)
            break

fich.close()