#===============================
# Avent of Code 2019 - Day 3
#
# Made by: Pedro Póvoa
# Date: 2/07/2020
#===============================

# === CODE ===
def Wiring(file):
    # wire variables
    curpos_x=0 # current position x
    curpos_y=0 # current position y
    
    wire=[]
    wire.append((0,0)) # 0,0 central port
    for size in range(0,len(file)):

        side = file[size][0] # letter
        num = int(file[size][1:]) # number
        
        # wire[][0] -> coord. x
        # wire[][1] -> coord. y
        if side == 'U': # incremet y axis
            aux=(curpos_x, curpos_y+num)

            curpos_y+=num # update y axis

        elif side == 'R': # incremet x axis
            aux=(curpos_x+num, curpos_y)

            curpos_x+=num # update x axis

        elif side == 'D': # decremet y axis
            aux=(curpos_x, curpos_y-num)

            curpos_y-=num # update y axis

        elif side == 'L': # decremet x axis
            aux=(curpos_x-num, curpos_y)

            curpos_x-=num # update x axis

        else:
            print("ERROR")

        wire.append(aux)

    return wire

#=== MAIN ===
fich= open('input.txt', 'r') # open 'input.txt' file

text= fich.read().split('\n')
text[0]= text[0].split(',')
text[1]= text[1].split(',')

wire1 = Wiring(text[0])
wire1 = list( dict.fromkeys(wire1) ) # remove duplicates

wire2 = Wiring(text[1])
wire2 = list( dict.fromkeys(wire2) ) # remove duplicates


points=[] # list of intersection coordinates

for i in range(0, len(wire1)-1):
    for j in range(0, len(wire2)-1):

        if wire1[i][0] == wire1[i+1][0]: # has the same x (vertical line)
            if wire2[j][1] == wire2[j+1][1]: # has the same y (the wires are perpendicular)

                if max(wire2[j][0],wire2[j+1][0]) >= wire1[i][0] >= min(wire2[j][0],wire2[j+1][0]):
                    if max(wire1[i][1],wire1[i+1][1]) >= wire2[j][1] >= min(wire1[i][1],wire1[i+1][1]):
                        points.append((wire1[i][0], wire2[j][1])) # intersection of the 'lines'
                        
        elif wire1[i][1] == wire1[i+1][1]: # has the same y (horizontal line)
            if wire2[j][0] == wire2[j+1][0]: # has also the same x (the wires are perpendicular)

                if max(wire2[j][1],wire2[j+1][1]) >= wire1[i][1] >= min(wire2[j][1],wire2[j+1][1]):
                    if max(wire1[i][0],wire1[i+1][0]) >= wire2[j][0] >= min(wire1[i][0],wire1[i+1][0]):
                        points.append((wire2[j][0], wire1[i][1])) # intersection of the 'lines'
       
print(points)

sum=[] # list of the distances
for p in points:
    sum.append(abs(p[0])+abs(p[1]))
#print(sum)

#print(points[sum.index(min(sum))]) # coordinates of the closest intersection of the center

print("Result:", min(sum))

fich.close()