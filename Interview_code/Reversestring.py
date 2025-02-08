Name = "Bhuvan"
print (Name[::-1])
print (Name[:-1])
print (Name[:1])

string = "radar"
print(string == string[::-1])

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
