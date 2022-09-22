""""
numbers = [1, 2, 3, -100, -10, 0, 4]

positive_numbers = 0
negative_numbers = 0

for i in numbers:
    if i > 0:
        positive_numbers += 1

for i in numbers:
    if i < 0:
        negative_numbers += 1


print(f'Negatives: {negative_numbers}, positives: {positive_numbers}')
"""

numbers = [1, 2, 3, -100, -10, 0, 4]

positive_numbers = 0
negative_numbers = 0

for i in numbers:
    if i > 0:
        positive_numbers += 1
    elif i < 0:
        negative_numbers += 1


print(f'Negatives: {negative_numbers}, positives: {positive_numbers}')