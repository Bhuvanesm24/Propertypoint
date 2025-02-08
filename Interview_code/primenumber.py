# n = int(input("Enter the number"))
# count = 0
# for i in range (1, n):
#     if n % i ==0:
#         count = count +1
# if count == 1:
#     print ("prime")
# else:
#     print("not a prime")
n= int(input("Enter the number"))
for i in range(2, n):
    if n % i == 0:
        print("not a prime")
        break
else:
    print("prime")

for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")





