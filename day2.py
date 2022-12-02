#!/usr/bin/python

def result(they, me):
    if (they == "A" and me == "Z") or (they == "B" and me == "X") or (they == "C" and me == "Y"): #Win
        return "Lose";
    if((they == "A" and me == "X") or (they == "B" and me == "Y") or (they == "C" and me == "Z")): #Draw
        return "Draw";
    if((they == "A" and me == "Y") or (they == "B" and me == "Z") or (they == "C" and me == "X")): #Lose
        return "Win";

def score(they, me, scores):
    return scores[me] + scores[result(they,me)]


scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "Win": 6,
    "Draw": 3,
    "Lose": 0,
}

input = open("input2.txt", "r")
lines = input.readlines();
sum = 0

for l in lines:
    sum = sum + score(l[0],l[2],scores)

print(sum)