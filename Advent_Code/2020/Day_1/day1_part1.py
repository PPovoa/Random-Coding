#===============================
# Avent of Code 2020 - Day 1
#
# Made by: Pedro Póvoa
# Date: 26/08/2021
#===============================

# === CODE ===
import math

# Part 1 ===
fich = open('input.txt', 'r')

table= fich.read().split('\n')

for num1 in table:
    for num2 in table:
        if num1 != '' and num2 != '':
            if int(num1)+int(num2) == 2020:
                print(num1, " * ", num2, " = ", int(num1)*int(num2))

fich.close()