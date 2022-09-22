"""
simple version
i = 0

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
"""

# if i % 3 == 0 -> "Fizz"
# if i % 5 == 0 -> "Buzz"
# if i % 7 == 0 -> "Bzz"

for i in range(1, 101):
    did_we_print_anything = False
    if i % 3 == 0:
        print("fizz")
        did_we_print_anything = True
    if i % 5 == 0:
        print("buzz")
        did_we_print_anything = True
    if i % 7 == 0:
        print("Bzz")
        did_we_print_anything = True

    if not did_we_print_anything:
        print(i)


