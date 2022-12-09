steps = {
    'U': (1, 0),
    'D': (-1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

H = [0, 0]
T = [0, 0]

tail_positions = set()

def follow(current_tail, new_head):
    
    if abs(current_tail[0] - new_head[0]) < 2 and \
       abs(current_tail[1] - new_head[1]) < 2:
       # head and tail are close enough
       return current_tail

    if current_tail[0] == new_head[0]:
        # move one horizontally
        return [current_tail[0], (current_tail[1] + new_head[1]) / 2]

    if current_tail[1] == new_head[1]:
        # move one vertically
        return [(current_tail[0] + new_head[0]) / 2, current_tail[1]]

    # move one diagonally
    x = current_tail[0] + 1 if current_tail[0] < new_head[0] else current_tail[0] - 1
    y = current_tail[1] + 1 if current_tail[1] < new_head[1] else current_tail[1] - 1

    return [x, y]

for move in (line.strip() for line in open("Day09.txt")):
    [direction, length] = move.split(' ')
    step = steps[direction]

    for i in range(0, int(length)):

        H = [H[0] + step[0], H[1] + step[1]]
        T = [int(c) for c in follow(T, H)]

        tail_positions.add((T[0], T[1]))
    
print(len(tail_positions))
