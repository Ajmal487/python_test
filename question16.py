#16. Write a program to find the longest word in a sentence.
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = "This is a simple sentence with some long words"
result = find_longest_word(sentence)
print(f"Longest word in the sentence: {result}")


