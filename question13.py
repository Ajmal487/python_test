#13. Write a program to find the first non-repeating character in a string.
def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
my_string = "hello"
result = first_non_repeating_char(my_string)
print(f"First non-repeating character in '{my_string}': {result}")