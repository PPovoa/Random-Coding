import math

# Part 2 ===

fich = open('input.txt', 'r')
total = 0

for i in fich.readlines():
    fuel = math.trunc(int(i)/3)-2
    while True:

        if fuel <= 0:
            break
        
        total += fuel
        fuel = math.trunc(fuel/3)-2

print("total =", total)

fich.close()