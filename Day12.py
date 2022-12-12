heights = []
start = (0, 0)
end = (0, 0)

for trimmed in (line.strip() for line in open('Day12.txt')):
    row = []
    for char in trimmed:
        if char == 'S':
            start = (len(heights), len(row))
            row.append(0)
        elif char == 'E':
            end = (len(heights), len(row))
            row.append(27)
        else:
            row.append(ord(char) - 96)

    heights.append(row)

min_depths = {}

def walk(from_height, x, y, depth):
    try:
        to_height = heights[x][y]

        if from_height + 1 >= to_height and \
            ((x, y) not in min_depths.keys() or min_depths[(x, y)] > depth):

            min_depths[(x, y)] = depth

            walk(to_height, x+1, y, depth+1)
            walk(to_height, x-1, y, depth+1)
            walk(to_height, x, y+1, depth+1)
            walk(to_height, x, y-1, depth+1)

    except:
        pass

walk(0, start[0], start[1], 0)

print(min_depths[end])