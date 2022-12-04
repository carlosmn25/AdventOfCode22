#!/usr/bin/python
import string

def find_repeated(comp1, comp2):
    appears_in_comp1 = {}
    for c in comp1:
        appears_in_comp1[c] = True;
    for c in comp2:
        if(c in appears_in_comp1): #Return the first character that appears in both halves
            return c

def find_badge(group_list): #Receives 3 lines and returns the only character that appears in all of them
    countdict = dict();
    for group in group_list:
        gindex = group_list.index(group);
        for character in group:
            if(character == '\n'): continue #ignore line breaks
            if(character not in countdict):
                countdict[character] = [False,False,False]
            countdict[character][gindex] = True
    
    for entry in countdict:
        if(countdict[entry] == [True,True,True]): return entry


alphabet = list(string.ascii_letters); #generate alphabet
priorities = dict();
for i in range(0,52):
    priorities[alphabet[i]] = i + 1 #fill priorities dict

#input = open("input3.txt", "r")
input = open("input3.txt", "r")
lines = input.readlines();
sum = 0

""" for line in lines:
    length = len(line)
    split_index = int((length/2))
    first = line[0:split_index]
    second = line[split_index:length]
    rep = find_repeated(first,second)
    sum += priorities[rep] """

group = 0;
group_list = []
for line in lines:
    if (group == int(lines.index(line)/3)): #Get group id
        group_list.append(line)
        if(int(lines.index(line)%3 == 2)):
            badge = find_badge(group_list) #Get the badge for the current group
            sum += priorities[badge]
    else:
        group_list = []
        group_list.append(line)
        group += 1;

print('The sum of all priorities is: ', sum)