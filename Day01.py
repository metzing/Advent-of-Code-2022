max = 0
sum = 0

for trimmed in (line.strip() for line in open('Day01.txt')):
    if len(trimmed) == 0:
        if (max < sum):
            max = sum
        sum = 0
    else:
        sum += int(trimmed)

print(max)
