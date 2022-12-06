#!/usr/bin/python
import queue
elements = queue.Queue()
input = open("input6.txt", "r")
text = input.readline()
#text = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
index = 0

for char in text:
    if(char in elements.queue):
        while char in elements.queue:
            elements.get() #Remove the first elements in the queue until the repeated one doesn't appear
        elements.put(char)
    elif(len(elements.queue) == 13): #Not found and it's the 14th char
        print(index + 1) #print the index of the character
        break
    else:
        elements.put(char);
    
    index+=1
