#6. Write a function to generate the Fibonacci series up to N terms.
def generate_fibonacci(n):
    fibonacci = [0, 1]
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]

N = int(input("Enter the number of terms: "))
print("Fibonacci series up to", N, "terms:")
print(generate_fibonacci(N))