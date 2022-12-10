import re

measures = [20, 60, 100, 140, 180, 220]

lines = [line.strip() for line in open('Day10.txt')]

busy = 0
offset = 0
cycle = 1
x = 1

results = []

while len(lines) > 0 or offset != 0:

    if busy == 0 and len(lines) != 0: 
        line = lines.pop(0)

        if line != 'noop':
            offset = int(re.match(r'addx (?P<offset>[0-9-]+)', line).group('offset'))
            busy = 2

    if cycle in measures:
        results.append((x * cycle))

    if busy > 0:
        busy -= 1

        if busy == 0:
            x += offset
            offset = 0

    cycle += 1

print(sum(results))
