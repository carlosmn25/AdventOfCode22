def ranges_overlap(r1start,r1end,r2start,r2end): #Exercise 1
    if((r1start >= r2start and r1end <= r2end) or (r2start >= r1start and r2end <= r1end)): return True
    return False

def any_overlapping(r1start,r1end,r2start,r2end): #Exercise 2
    if(r1start in range(r2start,r2end+1) or r1end in range(r2start,r2end+1) or r2start in range(r1start,r1end+1) or r2end in range(r1start,r1end+1)):
        return True
    return False



input = open("input4.txt", "r")
lines = input.readlines();

sum = 0
for l in lines:
    l = l.replace('\n','')
    ranges = l.split(',')
    limits = []
    for r in ranges:
        limits.append(r.split('-'))
    if(any_overlapping(int(limits[0][0]),int(limits[0][1]),int(limits[1][0]),int(limits[1][1]))): sum += 1

print(sum)