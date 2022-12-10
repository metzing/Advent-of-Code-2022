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
    return abs(((cycle - 1) % 40) - (x % 40)) <= 1

while len(lines) > 0 or offset != 0:

    if busy == 0 and len(lines) != 0: 
        line = lines.pop(0)

        print(f'Start {cycle}: begin {line}')

        if line != 'noop':
            offset = int(re.match(r'addx (?P<offset>[0-9-]+)', line).group('offset'))
            busy = 2

    
    print(f'During {cycle} cursor ')
    print(''.join(['#' if near(i, x) else '.' for i in range(0,40)]))

    if near(cycle, x):
        line_out += '#'
    else :
        line_out += '.'

    print(line_out)
     
    if cycle in linebreaks:
        output.append(line_out)
        line_out = ''

    if busy > 0:
        busy -= 1

        if busy == 0:
            x += offset
            offset = 0
            print(f'Cursor position:')
            print(''.join(['#' if near(i, x) else '.' for i in range(0,40)]))


    cycle += 1
    print()

print()
print()
print('\n'.join(output))