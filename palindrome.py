word = input("enter your word: ")
reverse =""
for char in word[-1::-1]:
    reverse += char
if reverse == word:
    print("palindrome")
else:
    print("not palindrome")