import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
# Sample text
text = "cats are chasing mice in the garden"
# Tokenize the text into words
words = word_tokenize(text)
# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()
# Define a function to convert POS tags to WordNet tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else: 
        return wordnet.NOUN
# Perform lemmatization
lemmatized_words = []
for word, pos in nltk.pos_tag(words):
    wordnet_tag = get_wordnet_pos(pos)
    lemma = lemmatizer.lemmatize(word, wordnet_tag)
    lemmatized_words.append(lemma)
# Print the lemmatized words
print(lemmatized_words)
