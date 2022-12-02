outcomePoints = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

guessPoints = {
    'A': {
        'X': 3,
        'Y': 1,
        'Z': 2,
    },
    'B': {
        'X': 1,
        'Y': 2,
        'Z': 3,
    },
    'C': {
        'X': 2,
        'Y': 3,
        'Z': 1,
    }
}

aggr = 0

for [enemy, _space, outcome] in (line.strip() for line in open('Day02.txt')):
    aggr += outcomePoints[outcome] + guessPoints[enemy][outcome]

print(aggr)