def valueOf(char: str) -> int:
    if char.islower():
        return ord(char) - 96 # ord('a') == 97
    else:
        return valueOf(char.lower()) + 26

aggr = 0

for sack in (line.strip() for line in open('Day03.txt')):
    left = sack[0 : (int(len(sack) / 2))]
    right = sack[int(len(sack) / 2) : len(sack)]

    found = list(l for l in left if l in right)[0]

    aggr += valueOf(found)

print(aggr)