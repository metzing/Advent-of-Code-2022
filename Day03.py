def value_of(char: str) -> int:
    if char.islower():
        return ord(char) - 96  # ord('a') == 97
    else:
        return value_of(char.lower()) + 26


groupSize = 3

sacks = list(line.strip() for line in open('Day03.txt'))
aggr = 0

for groupIndex in range(int(len(sacks) / groupSize)):

    [first, second, third] = sacks[groupIndex * groupSize: groupIndex * groupSize + groupSize]

    found = list(i for i in first if i in second and i in third)[0]

    aggr += value_of(found)

print(aggr)
