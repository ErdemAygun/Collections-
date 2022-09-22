
unique_numbers = set()

while True:
    string = input("enter a number or 'end' :")
    if string == 'end':
        break
    number = int(string)
    unique_numbers.add(number)

print(f"You've entered {len(unique_numbers)} unique numbers")

even_numbers = set()

for i in range(0, 101, 2):
    even_numbers.add(i)

print(f"You've entered {len(even_numbers & unique_numbers)} even numbers")







