import re
# sample text
text="Regular expressions are a Powerful tool for text processing. They can be used for pattern matching, tokenization, and more." 
#Define a regular expression pattern to match words
word_pattern = r'\w+'
#Find all words in the text the findall () function using 
words = re.findall (word_pattern, text)
# Print the list of words
print(words)
