import re

linebreaks = [40, 80, 120, 160, 200, 240]

lines = [line.strip() for line in open('Day10.txt')]

busy = 0
offset = 0
cycle = 1
x = 1

line_out = ''
output = []

def near(cycle, x):
    return abs((cycle % 40) - ((x + 1) % 40)) <= 1

while len(lines) > 0 or offset != 0:

    if busy == 0 and len(lines) != 0: 
        line = lines.pop(0)

        if line != 'noop':
            offset = int(re.match(r'addx (?P<offset>[0-9-]+)', line).group('offset'))
            busy = 2

    if near(cycle, x):
        line_out += '#'
    else :
        line_out += ' '

    if cycle in linebreaks:
        output.append(line_out)
        line_out = ''

    if busy > 0:
        busy -= 1

        if busy == 0:
            x += offset
            offset = 0
    cycle += 1

print('\n'.join(output))