count = 0

for stripped in (line.strip() for line in open('Day04.txt')):
    [left_start, left_end, right_start, right_end] = \
        [int(boundary) for assignment in stripped.split(',') for boundary in assignment.split('-')]

    left = range(left_start, left_end + 1)
    right = range(right_start, right_end + 1)

    if all(l in right for l in left) or all(r in left for r in right):
        count += 1

print(count)