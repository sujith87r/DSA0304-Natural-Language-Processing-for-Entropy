import nltk
from nltk.corpus import wordnet

# Create a list of all word classes
word_classes = ['noun', 'verb', 'adjective', 'adverb', 'open', 'closed']

# Create a dictionary of word classes to pos tags
pos_tags = {
    'n': 'NN',  # Mapping 'n' for noun
    'v': 'VB',  # Mapping 'v' for verb
    'a': 'JJ',  # Mapping 'a' for adjective
    'r': 'RB',  # Mapping 'r' for adverb
    'u': 'UH',  # Mapping 'u' for interjection
}

# Create a function to tag a word with its POS
def tag_word(word):
    # Get the word's synsets
    synsets = wordnet.synsets(word)
    if synsets:
        # If synsets are found, get the first one's POS tag
        pos_tag = pos_tags.get(synsets[0].pos())
        # Return the word and its POS tag
        return word, pos_tag
    else:
        return word, None

# Create a function to tag a sentence with POS tags
def tag_sentence(sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)
    # Tag each word in the sentence
    tagged_words = [tag_word(token) for token in tokens]
    # Return the tagged sentence
    return tagged_words

# Create a function to print the tagged sentence
def print_tagged_sentence(tagged_sentence):
    # Print the tagged sentence
    for word, pos_tag in tagged_sentence:
        if pos_tag:
            print(f'{word} / {pos_tag}')
        else:
            print(f'{word} / <Not found>')

# Download the averaged perceptron tagger model (if not already downloaded)
nltk.download('averaged_perceptron_tagger')

sentence = 'the boy was playing football in the rain'
tagged_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
print_tagged_sentence(tagged_sentence)
