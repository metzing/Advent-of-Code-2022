i = 4
while len(set(open('Day06.txt').readline()[i-4:i])) != 4:
    i += 1
print(i)