#table = [3, 6, 19, 4, 1, 0, 5]

table = []
for i in range (1, 100, 17):
    table.append(i % 23)

largest_idx = 0
smallest_idx = 0
for i in range(len(table)):
    print(f"{i}: {table[i]}")
    if table[i] > table[largest_idx]:
        largest_idx = i
    if table[i] < table[smallest_idx]:
        smallest_idx = i

print(table)

table[largest_idx], table[smallest_idx] = table[smallest_idx], table[largest_idx]

print(table)

