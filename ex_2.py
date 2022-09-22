numbers = []

while len(numbers) < 10:
    number = int(input('provide numbers:'))
    numbers.append(number)

average = sum(numbers) / len(numbers)

print(f'The average from the provided numbers equals {average:.2f}')
