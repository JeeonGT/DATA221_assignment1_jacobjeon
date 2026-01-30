from random import random

values = [random() for i in range(20)]
x = random()
values = (sorted(values))
for value in values:
    if value >= x:
        index_matching_condition = values.index(value)
        print(f"{index_matching_condition} matches the condition for {x}")

print(values)
