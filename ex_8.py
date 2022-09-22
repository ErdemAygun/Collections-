text = input("write a word:")

word = {}

for letter in text:
    if letter in word:
        word[letter] +=1
    else:
        word[letter] = 1
print(word)

