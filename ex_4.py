how_many = 0
for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        how_many += 1
        print(how_many)