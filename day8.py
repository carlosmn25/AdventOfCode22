def is_visible(list, value):
    if len(list) == 0:
        return True
    return value > max(list)


#read data from file input8.txt:
input = open("input8.txt", "r")
lines = input.readlines();

#initialize the 2D array with heights of the trees
w = len(lines[0])
h = len(lines)
trees = [[0 for x in range(w - 1)] for y in range(h)]

i = 0;
for l in lines:
    j = 0;
    for c in l:
        if (c != "\n"):
            trees[i][j] = int(c)
        j = j + 1
    i = i + 1

r = 0;
visibles = 0;
for row in trees:
    t = 0;
    for tree in row:
        col_up = []
        for i in range(0,r):
            col_up.append(trees[i][t])
        col_down = []
        for i in range(r+1,h):
            col_down.append(trees[i][t])
        if is_visible(row[0:t], tree) or is_visible(row[t+1:], tree) or is_visible(col_up, tree) or is_visible(col_down, tree):
            visibles = visibles + 1;
        t = t + 1
    r = r + 1

print(visibles)

