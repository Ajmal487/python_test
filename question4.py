#4. Write a program to check whether two strings are anagrams.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

if len(string1) != len(string2):
    print("The strings are not anagrams.")
else:
    if sorted(string1) == sorted(string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")