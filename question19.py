#19. Write a program to count the occurrence of each word in a text file.
from collections import Counter
import re

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\b[a-z]+\b', text)
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}

sample_text = """Python is great. Python is powerful.
Python is easy to learn. I love Python."""

with open('sample.txt', 'w') as f:
    f.write(sample_text)

word_counts = count_words_in_file('sample.txt')
print("Word Occurrences:")
for word, count in sorted(word_counts.items()):
    print(f"  {word}: {count}")
