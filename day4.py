def ranges_overlap(r1start,r1end,r2start,r2end):
    if((r1start >= r2start and r1end <= r2end) or (r2start >= r1start and r2end <= r1end)): return True
    """ if((r1start >= r2start) and (r1end <= r2end)): return True
    elif (r2start >= r1start and r2end <= r1end): return True """
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
    if(ranges_overlap(int(limits[0][0]),int(limits[0][1]),int(limits[1][0]),int(limits[1][1]))): sum += 1

print(sum)