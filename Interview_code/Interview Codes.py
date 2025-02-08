'''Reverse a string: Write a program to reverse a string without using built-in functions.

string = "Hello"
reversed_string = string[::-1]
print(reversed_string)

Check for palindrome: Write a program to check if a string is a palindrome.

string = "radar"
print(string == string[::-1])

FizzBuzz: Write a program that prints numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz."

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)