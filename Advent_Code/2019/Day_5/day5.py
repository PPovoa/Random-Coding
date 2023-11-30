#===============================
# Avent of Code 2019 - Day 5
#
# Made by: Pedro Póvoa
# Date: 30/11/2023
#===============================

# === CODE ===
import math

POSITION_MODE = 0
IMMEDIATE_MODE = 1

def GetValueFromParameters(current_Pointer, program, parametersModes):
    values=[]
    for parameter in reversed(parametersModes):
        if int(parameter)==POSITION_MODE:
            position_Value = int(program[current_Pointer])
            values.append(int(program[position_Value]))

        elif int(parameter)==IMMEDIATE_MODE:
            values.append(int(program[current_Pointer]))
        current_Pointer += 1

    return current_Pointer, values


"""
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
"""
def main():
    current_Pointer = 0 # current position of the pointer
    input_instruction = "5"

    fich= open('input.txt', 'r') # open 'input.txt' file
    program = fich.read().split(',')
    fich.close()

    while True:
        instruction = program[current_Pointer]
        size_instruction = len(instruction)
        opCode = int(instruction[size_instruction-2:]) # last 2 digits are the opCode
        parametersModes = instruction[:size_instruction-2]
        parametersModes = parametersModes.zfill(2) # add zeros to the beginning of the string until it reaches the 2 digits
        
        current_Pointer += 1 # next number

        if opCode == 1: # adding operation
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            position_Value = int(program[current_Pointer]) # position that will suffer changes
            program[position_Value] = str(values[0]+values[1])
            
        elif opCode == 2: # multipling operation
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            position_Value = int(program[current_Pointer]) # position that will suffer changes
            program[position_Value] = str(values[0]*values[1])

        elif opCode == 3: # input instruction
            position_Value = int(program[current_Pointer]) # position that will suffer changes
            program[position_Value] = input_instruction
            
        elif opCode == 4: # output instruction
            if int(parametersModes[-1])==POSITION_MODE:
                position_Value = int(program[current_Pointer])
                output_instruction = int(program[position_Value])

            elif int(parametersModes[-1])==IMMEDIATE_MODE:
                output_instruction = int(program[current_Pointer])

            if output_instruction!=0 and int(program[current_Pointer+1])!=99:
                print("ERRO - curr:", current_Pointer, "program[current_Pointer]:", program[current_Pointer], "output: ", output_instruction)

            else:
                position_Value = int(program[current_Pointer])
                output_instruction = int(program[position_Value])
        
        # part2
        elif opCode == 5: #jump-if-true -> first parameter is non-zero
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            if int(values[0]) != 0:
                current_Pointer = int(values[1]) # jump to the value of the second number
            continue

        elif opCode == 6: #jump-if-false -> first parameter is zero
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            if int(values[0]) == 0:
                current_Pointer = int(values[1]) # jump to the value of the second number
            continue

        elif opCode == 7: #less than -> first parameter is less than the second parameter
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            position_Value = int(program[current_Pointer])
            if int(values[0]) < int(values[1]):
                program[position_Value] = "1"
            else:
                program[position_Value] = "0"

        elif opCode == 8: #equals -> first parameter is equal to the second parameter
            current_Pointer, values = GetValueFromParameters(current_Pointer, program, parametersModes)
            position_Value = int(program[current_Pointer])
            if int(values[0]) == int(values[1]):
                program[position_Value] = "1"
            else:
                program[position_Value] = "0"

        elif opCode == 99: # halt the program
            print("Diagnostic Code: ", output_instruction)
            break

        else:
            print("ERRO - curr:", current_Pointer, "program[current_Pointer]:", program[current_Pointer], "opCode:", opCode)
            break
        
        current_Pointer += 1

if __name__ == "__main__":
    main()

