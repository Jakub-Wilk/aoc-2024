import re

with open("1.txt") as f:
    puzzle = f.read()

numbers = [int(num) for num in re.findall(r"\d+", puzzle)]

list1 = numbers[::2]
list2 = numbers[1::2]

similarity_dict = {}
for n in list2:
    if n in similarity_dict:
        similarity_dict[n] += 1
    else:
        similarity_dict[n] = 1

for k, v in similarity_dict.items():
    similarity_dict[k] = k * v

final_list = [similarity_dict[n] if n in similarity_dict else 0 for n in list1]

print(sum(final_list))
