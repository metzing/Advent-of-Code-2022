rows = []

for trimmed in (line.strip() for line in open('Day08.txt')):
    rows.append([])
    for height in (int(char) for char in trimmed):
        rows[-1].append(height)

internal_visible = 0

for i in range(1, len(rows) - 1):
    for j in range(1, len(rows[i]) - 1):
        current = rows[i][j]

        left = rows[i][0:j]
        right = rows[i][j + 1:len(rows[i])]
        top = [rows[k][j] for k in range(0, i)]
        bottom = [rows[k][j] for k in range(i+1, len(rows))]
        if max(left) < current or max(right) < current or max(top) < current or max(bottom) < current:
            internal_visible += 1

externally_visible = (len(rows) + len(rows[i])) * 2 - 4

print(internal_visible + externally_visible)
