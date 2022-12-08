rows = []

for trimmed in (line.strip() for line in open('Day08.txt')):
    rows.append([])
    for height in (int(char) for char in trimmed):
        rows[-1].append(height)

def count_lt(than, list, reverse):
    if(reverse):
        list.reverse()

    if len(list) == 0:
        return 0
    
    count = 0

    for i in list:
        if (i < than):
            count += 1
        else:
            count += 1
            return count
    
    return count

max_score = 0

for i in range(1, len(rows) - 1):
    for j in range(1, len(rows[i]) - 1):
        current = rows[i][j]
        
        left = count_lt(current, rows[i][0:j], True)
        right = count_lt(current, rows[i][j + 1:len(rows[i])], False)
        top = count_lt(current, [rows[k][j] for k in range(0, i)], True)
        bottom = count_lt(current, [rows[k][j] for k in range(i + 1, len(rows))], False)
        
        max_score = max(max_score, left * right * top * bottom)

print(max_score)
