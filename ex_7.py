"""
wrong way
word = input("write a word:")

real_word = (f'Marry had a <{word}> lamp')

count = 0

for letter in word:
    if letter in real_word:
        count +=1

print(real_word)
print(f'number of letters: {count}')
"""
text = input('input text containing a pair of <> brackets:')

are_we_inside_brackets = False
count = 0

for letter in text:
    if letter == "<":
        are_we_inside_brackets = True
    elif letter == ">":
        are_we_inside_brackets = False
    elif are_we_inside_brackets:
            count += 1

print(f'there are {count} characters between <>')

