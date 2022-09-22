"""
In the interactive environment session, create the following data
structures using comprehension expressions:
- a list containing floating point numbers from 0.0 to 1.0 with
increments of 0.1
- a set of tuples containing 3 elements each - a given number, its
square and its cube - in the range from -10 to 10
- a dictionary created from set of strings that maps strings to
their length
"""
print([i / 10 for i in range(11)])

print({(i, i ** 2, i ** 3) for i in range(-10,10)})

strings = {"butter", "well", "carrot", "mom", "python"}

print({i: len(i) for i in strings})