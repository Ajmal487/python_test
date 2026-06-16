#3. Write a program to count the frequency of each character in a string.
string = input("Enter a string: ")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")