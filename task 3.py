word = input("Enter a word: ")
lowercase_word = word.lower()

if lowercase_word == lowercase_word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
