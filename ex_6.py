string = input("provide a word: ")

vowels = ('a', 'e', 'i', 'o', 'u')

count = 0

for i in string:
    if i.lower() in vowels:
        count += 1

print(f'number of vowels in word : {count} ')







