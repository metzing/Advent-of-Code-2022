i = 14
while len(set(open('Day06.txt').readline()[i-14:i])) != 14:
    i += 1
print(i)