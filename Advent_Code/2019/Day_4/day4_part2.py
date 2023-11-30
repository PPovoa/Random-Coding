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
    groups = [] # save the pairs of consecutive numbers
    num_groups = 0

    not_asc = 0
    val_dup = 0
    if len(str(i)) <= 6: # not needed
        for j in range(0, 5):
            if str(i)[j] > str(i)[j+1]: # see if the numbers are ordered in ascending order
                not_asc = 1
                break

            if str(i)[j] == str(i)[j+1]: # see if exists two identical consecutive numbers
                val_dup = 1
                num_groups += 1
            
            if str(i)[j] != str(i)[j+1] or j==4: # 'j==4' to save the pairs of consecutive numbers in the last iteration of the loop
                if num_groups != 0:
                    groups.append(num_groups)
                num_groups=0
        
        if not_asc == 0 and val_dup == 1: # append when the numbers are in ascending order and there are two identical consecutive numbers
            for a in groups:
                if a == 1: # there is exactly one par in the number
                    code.append(i)
                    break
            
#print(code)
print("Result:",len(code))