#9. Write a program to find the missing number in a sequence.
numbers = [1, 2, 3, 5, 6]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
print(actual_sum)
missing_number = expected_sum - actual_sum
print("Missing number:", missing_number)