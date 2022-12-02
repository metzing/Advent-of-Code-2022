outcomePoints = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    }
}

guessPoints = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

aggr = 0

for [enemy, _space, guess] in (line.strip() for line in open('Day02.txt')):
    aggr += outcomePoints[enemy][guess] + guessPoints[guess]

print(aggr)