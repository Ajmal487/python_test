#14. Write a program to count vowels and consonants in a string.
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

my_string = "hello"
vowels, consonants = count_vowels_consonants(my_string)
print(f"Vowels in '{my_string}': {vowels}")
print(f"Consonants in '{my_string}': {consonants}")
