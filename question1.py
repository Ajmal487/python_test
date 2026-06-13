#1.Write a program to find the second largest number in a list.
numbers = [4, 1, 7, 3, 7, 2]
unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Need at least two different numbers")
else:
    print("Second largest number:", unique_numbers[-2])