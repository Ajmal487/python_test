#2.Write a program to remove duplicate elements from a list without using set().
numbers = [4, 1, 7, 3, 7, 2]
numbers.sort()
i = 1
while i < len(numbers):
    if numbers[i] == numbers[i-1]:
        numbers.pop(i)
    else:
        i += 1
print("List after removing duplicates:", numbers)
