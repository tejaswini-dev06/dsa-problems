number = int(input("enter your number: "))
factorial = number
for number in range(1,number):
    factorial *= number
print(factorial)