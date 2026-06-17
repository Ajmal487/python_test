#5. Write a program to find all prime numbers between 1 and N.
N = int(input("Enter a number: "))

for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")