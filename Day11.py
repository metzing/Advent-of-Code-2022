from functools import reduce
import re
from math import floor, lcm

monkeys = []
monkey_lcm = 1

class Monkey:
    def __init__(self, lines):
        self.index = int(re.fullmatch(r'Monkey (?P<index>\d):', lines[0]).group('index'))
        self.items = [int(worry_level) for worry_level in lines[1].lstrip('  Starting items:').split(', ')]
        [self.left, self.operation, self.right] = lines[2].split(' ')[-3:]
        self.divisor = int(lines[3].split(' ')[-1])
        self.true_recipient = int(lines[4].split(' ')[-1])
        self.false_recipient = int(lines[5].split(' ')[-1])
        self.inspect_count = 0

    def on_round(self):
        while len(self.items) > 0:
            self.inspect_count += 1
            item = self.items.pop(0)

            item = self.apply_operation(item) % monkey_lcm

            monkeys[self.true_recipient if item % self.divisor == 0 else \
                self.false_recipient].items.append(item)
    
    def apply_operation(self, item):
        operation = lambda left, right: left * right
        if self.operation == '+':
            operation = lambda left, right: left + right
        
        left = item if self.left == "old" else int(self.left)
        right = item if self.right == "old" else int(self.right)

        return operation(left, right)


    def __str__(self) -> str:
        return f'{self.index} - {",".join(map(str, self.items))}'

monkey_lines = []

for trimmed in (line.strip() for line in open('Day11.txt')):
    if trimmed == '':
        monkeys.append(Monkey(monkey_lines))
        monkey_lines = []
    else:
        monkey_lines.append(trimmed)

monkey_lcm = reduce(lambda aggr, monkey: lcm(aggr, monkey.divisor), monkeys, monkey_lcm)

for _ in range(10000):
    for monkey in monkeys:
        monkey.on_round()

numbers_of_inspection = [monkey.inspect_count for monkey in monkeys]

numbers_of_inspection.sort(reverse=True)
print(numbers_of_inspection[0]*numbers_of_inspection[1])