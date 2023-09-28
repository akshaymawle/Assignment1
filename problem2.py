# 2) Write a Python program that accepts a word from the user and reverse it.



# Input from user
word = input("enter a word")

reversed_word = ""     #empty string to store reversed word
index = len(word) - 1

# while loop.
while index >= 0:
    reversed_word += word[index]
    index -= 1
    
print("reversed word is", reversed_word)