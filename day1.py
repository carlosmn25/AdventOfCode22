#!/usr/bin/python

input = open("input.txt", "r")
lines = input.readlines();

max = 0;
sum = 0;

for l in lines:
    if (l != "\n"):
        l = l.strip(); #remove whitespaces
        currentn = int(l)
        sum = sum + currentn
        if(sum > max):
            max = sum
    else:
        sum = 0;

input.close();
print("The max number of calories is " + str(max))