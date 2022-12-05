import re

originalStackLines = []
instructionLines = []
aggr = originalStackLines

for trimmed in (line.strip() for line in open("Day05.txt")):
    if trimmed == '':
        aggr = instructionLines
    else:
        aggr.append(trimmed)

numberOfStacks = len(originalStackLines[-2].split(' '))
stacks = [list() for _ in range(numberOfStacks)]

originalStackLines.reverse()

for line in originalStackLines[1:]:
    for i in range(numberOfStacks):
        charIndex = i * 4 + 1
        if (charIndex <= len(line) - 1) and line[charIndex] != ' ':
            stacks[i].append(line[charIndex])

for instruction in instructionLines:
    [numberOfCrates, fromStack, toStack] = (int(num) for num in re.findall(r'\d+', instruction))

    for _ in range(numberOfCrates):
        stacks[toStack - 1].append(stacks[fromStack - 1].pop())

print(''.join(stack.pop() for stack in stacks))
