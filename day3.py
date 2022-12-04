#!/usr/bin/python
import string

def find_repeated(comp1, comp2):
    appears_in_comp1 = {}
    for c in comp1:
        appears_in_comp1[c] = True;
    for c in comp2:
        if(c in appears_in_comp1): #Return the first character that appears in both halves
            return c

alphabet = list(string.ascii_letters); #generate alphabet
priorities = dict();
for i in range(0,52):
    priorities[alphabet[i]] = i + 1 #fill priorities dict

input = open("input3.txt", "r")
#input = open("test3.txt", "r")
lines = input.readlines();
sum = 0

for line in lines:
    length = len(line)
    split_index = int((length/2))
    first = line[0:split_index]
    second = line[split_index:length]
    rep = find_repeated(first,second)
    sum += priorities[rep]

print("======================")
print(sum)
print(len(lines))