num = int(input("Enter a number: "))

isPrime = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            isPrime = True
            break

if isPrime:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
