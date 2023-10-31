import nltk
from nltk import CFG

# Define a CFG that includes "but" as a conjunction
grammar = CFG.fromstring("""
S -> NP VP | S 'but' S
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'house'
V -> 'chased' | 'saw'
""")

# Create a parser based on the modified CFG
parser = nltk.ChartParser(grammar)

def parse_sentence(sentence):
    tokens = sentence.split()
    for tree in parser.parse(tokens):
        tree.pretty_print()

# Example usage with sentences using "but":
sentence1 = "the cat chased a dog but a dog saw the house"
sentence2 = "a cat chased the dog but a dog chased a house"
parse_sentence(sentence1)
parse_sentence(sentence2)
