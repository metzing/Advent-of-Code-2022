sums = []
aggr = 0

for trimmed in (line.strip() for line in open('Day01.txt')):
    if len(trimmed) == 0:
        sums.append(aggr)
        aggr = 0
    else:
        aggr += int(trimmed)

sums.sort(reverse=True)

print(sum([sums[0], sums[1], sums[2]]))
