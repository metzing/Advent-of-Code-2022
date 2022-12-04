import re

count = 0

for stripped in (line.strip() for line in open('Day04.txt')):
    [left_start, left_end, right_start, right_end] = [int(boundary) for boundary in re.split(',|-', stripped)]

    left = range(left_start, left_end + 1)
    right = range(right_start, right_end + 1)

    if any(l in right for l in left) or any(r in left for r in right):
        count += 1

print(count)