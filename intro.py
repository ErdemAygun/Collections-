# Data structures  - collections

# Tuple
# - ordered
# - immutable - we cannot change the content of the tuple after we created it

#     0, 1, 2
a = (10,20,30)
print(a)
print(type(a))

# access operator -> []

print(a[1])
print(a[0])

b = (10, 25.0, 'erdem', True, None)
print(b)
print(b[3])

c = ((1,2), ('a','b','c'), (True, False))
print(c)
print(c[1][2])

# SLICING

d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

print(d[0])
print(d[1:3]) # left-closed, right-open
print(d[1:5])
print(d[1:10])
print(d[:4])
print(d[4:])
print(d[-4:-1])
print(d[5:-2])
print(d[0:9:2])
print(d[::2])
print(d[::-1])
print(d.index('e'))
print(len(d))

e = (1,2,3,4,5)
print(max(e))
print(min(e))
print(sum(e))

f = (1,2,3)
g = (4,5,6)
h = f + g
print(h)

i = f * 3
print(i)

# LIST
# - mutable
# - ordered

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# access operator [] - it works exactly same as for tuples

print(a[0])
print(a[::-1])

# we can change the content of the lists

a[0] = 1
print(a)

a.append(110)
print(a)

a.insert(1, 12)
print(a)

a.extend([200, 210, 220])
print(a)

a += [300, 310, 320]
print(a)

print(a)
a[1:3] = [1, 2]
print(a)

del(a[0])
print(a)

del(a[0:3])
print(a)

a.remove((310))
print(a)

a.sort(reverse=True)
print(a)

# empty list creation

a = []
a = list()

# how we can iterate through a list (or tuple)
# we can leverage for loop

list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for number in list_of_numbers:
    print(number)

tuple_of_numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
for number in tuple_of_numbers:
    print(number)

list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for index, number in enumerate(list_of_numbers):
    print(f'{index} = {number}')

# range function
for i in range(11):
    print(i)

for i in range(-5,6):
    print(i)

for i in range(-5,6,2):
    print(i)

list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30]

for number_a in list_a:
    for number_b in list_b:
        print(f'{number_a} + {number_b} = {number_a + number_b}')

# We can treat srrings as collection of characters
my_string = "to be or not to be"

# access operator
print(my_string[0])
print(my_string[1:3])
print(my_string[::-1])

print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string.capitalize())

numbers = [10, 20, 30, 40]

print(type(numbers))

string = "asdf"

print(f"{len(string) = }")

print(type(f"{string[1] = }"))

for character in string:
    print(character)


# in operator - checks for existence of an element within the collection

numbers = [10, 20, 30, 40]

print(f"{10 in numbers = }")
print(f"{15 in numbers = }")
print(f"{1020 in numbers = }")

string = "Mary had a little lamb"
print(f'{"a" in string = }')
print(f'{"lit" in string = }')

character = list(string)
print(f'{character =}')
print(f'{"lit" in character = }')

# DICTIONARIES

empty = {}

print(type(empty))

price = {"bread": 3, "carrot": 1.5}

print(price)
print(f'{price["bread"] = }')
print(f'{price["carrot"] = }')

# adding new key value pair
price["water"] = 7 # this will add a new key "water"
print(f'{price["water"]}')
print(price)

# modifying values
price["water"] += 3 # this requires that " water" is already a key in the dictionary
print(price)

price[10] = ["asdf", 103]
print(f'{price = }')

price[True] = "Truth is priceless"
print(f"{price = }")

for key in price:
    print(f'{key = }, value = {price[key]}')

# dictionaries in for loop
for kv in price.items():
    #k, v = kv
    k = kv[0]
    v = kv[1]
    print(k, v)

print("-" * 43)

for k, v in price.items():
    print(k, v)

# check for key's existence
print(f"{'water' in price = }")
print(f"{'cheese' in price = }")

# SET

# sets are mutable and unordered.

empty = set()

#empty = {} this is a dictionary, not a set

numbers = {10, 3, 14, 12, 1, 2}

print(numbers)
print(type(numbers))
print({"one", "two", "three", "four", "five"}) # sets are unordered

numbers.add(20)
print(f"{numbers = }")
numbers.add(20) # sets store only unique elements, so this line does nothing
print(f"{numbers = }")
print(f"{len(numbers)}")

text = "Mary had a little lamb"
unique = set()
for character in text:
    unique.add(character)
print(unique)

print(f"{set(text) =}")

# Set Operators

A = {1, 2, 3}
B = {3, 4, 5}
print(f"{A =}")
print(f"{B =}")
print(f"{A | B =}") # union - every element from both sets
print(f"{A - B =}") # difference - every element from A that is not in B
print(f"{B - A =}")
print(f"{A & B =}") # intersection - every element that is in both A and B
print(f"{A ^ B =}") # symetric difference - every element that appears in A or B but in both
print(f"{(A - B) | (B - A) =}")

# COMPREHENSION EXPRESSIONS
print('-' * 45)

table = [i % 23 for i in range (1, 100, 17)]
print(table)
print([i ** 2 for i in range(0,10)])

print({i ** 2 for i in range(-5, 5)}) # set
print({i: i % 3 == 0 for i in table}) # dict

#tab = []
#for i in range(20):
#    if i % 3 == 0 or i % 5 == 0:
#        tab.append(i)

print(f"{[i for i in range(20) if i % 3 == 0 or i % 5 == 0]} =") # list comprehension with 'if'

print(f"{[f'{x} x {y} = {x * y}' for x in range(4) for y in range(4)]}")







