#!/usr/bin/python

input = open("input.txt", "r")
lines = input.readlines();

max = 0;
sum = 0;
calories_list = [];

for l in lines:
    if (l != "\n"):
        l = l.strip(); #remove whitespaces
        currentn = int(l)
        sum = sum + currentn
        if(sum > max):
            max = sum
    else:
        calories_list.append(sum) #store last result and reset
        sum = 0;

input.close();
calories_list = sorted(calories_list, reverse=True)
print("The Top 3 calories are {t1}, {t2} and {t3}!!!".format(t1=calories_list[0], t2=calories_list[1], t3=calories_list[2]))
print("The addition of Top 3 is: {add}".format(add=(calories_list[0] + calories_list[1] + calories_list[2])))