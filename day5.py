#!/usr/bin/python
import string
from collections import deque
""" 1) Lista de pilas con tantas pilas como columnas haya en el archivo de entrada
2) Rellenar cada pila con su configuración inicial
3) Función que interprete los movimientos
	- Usar split con separador ' '
4) Función que ejecute los movimientos (move(howmany,from,to))
5) Cuando haya acabado de encontrar líneas: sacar el primero de cada pila y concatenarlos
6) Replace '[' y ']' por '' """

def get_initial_config(line_list): #Returns a list of stacks with the initial config
    base = 0
    for l in line_list:
        clean = l.replace(' ','')
        if(clean[0] != '1'): continue
        else:
            base = line_list.index(l) #store index of the last line in initial config
            break
    
    columns = len(line_list[base].replace(' ','').replace('\n','')) #get how many stacks are there
    
    #initialize stack list
    stack_list = []
    for i in range(0,columns): 
        stack_list.append(deque())

    for line in reversed(line_list[0:base]):
        for char in range(0,len(line)):  #iterate over the characters in the line
            if(line[char] in list(string.ascii_uppercase)): #if it is a letter
                stack_list[(char - 1)//4].append(line[char])    #introduce the letter in the corresponding stack
                                                                #Indexes 1 5 9 13... -> divide by 4 to get index of stack in list
    return stack_list

def procedure_begin_index(line_list): #Returns the line number in which the orders to arrange stacks begin
    for line in line_list:
        if(line[0] in list(string.ascii_letters)): #if first char in the line is a letter
            return line_list.index(line) #return the index of the current line
    return -1 #Error: not found

def execute_movement(text, stack_list): #Interprets the movement specified in the received text
    words = text.split()
    move(int(words[1]), int(words[3]), int(words[5]), stack_list) #Send the numbers to the move function
    return

def move(howmany,origin,destination, stack_list): #Moves "howmany" elements from origin to destination
    for i in range(0,howmany):
        stack_list[destination - 1].append(stack_list[origin - 1].pop())
    return

def top_in_each_stack(stack_list):
    result = ''
    for s in stack_list:
        pop = s.pop()
        result = result + pop
    return result
        

input = open("input5.txt", "r")
lines = input.readlines()
crate_stacks = get_initial_config(lines);

begin_index = procedure_begin_index(lines)
for line in lines[begin_index:]: #start iterating from the beginning of the instructions
    execute_movement(line,crate_stacks)

print(top_in_each_stack(crate_stacks))
