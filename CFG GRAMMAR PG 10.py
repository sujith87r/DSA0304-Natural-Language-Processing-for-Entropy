import nltk
from nltk.parse.generate import generate
from nltk import CFG

# Define a simple CFG for NP and VP
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'house'
V -> 'chased' | 'saw'
""")

# Create a parser based on CFG
parser = nltk.ChartParser(grammar)

# Define a sentence to parse
sentence = "the cat chased a dog"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
