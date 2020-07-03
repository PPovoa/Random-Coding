#===============================
# Avent of Code 2019 - Day 4
#
# Made by: Pedro Póvoa
# Date: 03/07/2020
#===============================

# === CODE ===
fich= open('input.txt', 'r') # open 'input.txt' file

[min,max]= fich.read().split('-')

fich.close()

code=[] # list of possible codes

for i in range(int(min), int(max)):
    not_asc = 0
    val_dup = 0
    if len(str(i)) <= 6: # not needed
        for j in range(0, 5):
            if str(i)[j] > str(i)[j+1]: # see if the numbers are ordered in ascending order
                not_asc = 1
                break

            if str(i)[j] == str(i)[j+1]: # see if exists two identical consecutive numbers
                val_dup = 1
        
        if not_asc == 0 and val_dup == 1: # append when the numbers are in ascending order and there are two identical consecutive numbers
            code.append(i)

print(code)
print(len(code))