import math

# Part 1 ===

fich = open('input.txt', 'r')
total = 0

for i in fich.readlines():    
    total += math.trunc(int(i)/3)-2

print("total =", total)

fich.close()