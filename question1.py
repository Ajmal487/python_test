#1.Write a program to find the second largest number in a list.
numbers = []
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Second largest number:", unique_numbers[-2])