# 12 - 4 - 24
# split four digit number 
# num = 1234 -> first = 1, sec = 2, third = 3, fourth = 4

num = 0
num1 = 0
num2 = 0
first = 0
sec = 0
third = 0
fourth = 0

num = int(input("Enter a four digit number : "))

# filter = int(num / 1000)
# sec = int(num / 100)
# third = int(num / 10)
# fourth = num % 10


num1 = int(num / 100)
num2 = int(num % 100)

first = int(num1 / 10)
sec = num1 % 10

third = int(num2 / 10)
fourth = num2 % 10

print(f"first digit of {num} is {first}, second digit is {sec}, third digit is {third} and fourth digit is {fourth} ")

# Enter a four digit number : 1234
# first digit of 1234 is 1, second digit is 2, third digit is 3 and fourth digit is 4
