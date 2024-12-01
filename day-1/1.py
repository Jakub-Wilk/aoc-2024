import re

with open("1.txt") as f:
    puzzle = f.read()

numbers = [int(num) for num in re.findall(r"\d+", puzzle)]

list1 = sorted(numbers[::2])
list2 = sorted(numbers[1::2])

diffs = [abs(pair[0] - pair[1]) for pair in zip(list1, list2)]

print(sum(diffs))
