from collections import Counter
import re

# Define a list of stop words
stop_words = set(["the", "and", "or", "but", "to", "of", "a", "an", "in", "on", "for", "with", "as", "by", "at"])

# Open the file in read mode
with open('paragraphs.txt', 'r') as file:
    # Read the entire text, remove non-alphanumeric characters, split it into words
    words = re.findall(r'\b\w+\b', file.read())

# Remove stop words from the list of words
words = [word for word in words if word.lower() not in stop_words]

# Calculate the frequency of each word using Counter
word_freq = Counter(words)

# Display the word frequencies
for word, freq in word_freq.items():
    print(word + ": " + str(freq))