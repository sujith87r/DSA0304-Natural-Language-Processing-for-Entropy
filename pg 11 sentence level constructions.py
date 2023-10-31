import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the input sentence
sentence = "The cat on the roof, purring softly, which belongs to my neighbor caught a mouse."

# Parse the sentence
doc = nlp(sentence)

# Iterate through tokens and print token information
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}")

# Define lists to store different types of phrases
prepositional_phrases = [chunk.text for chunk in doc.noun_chunks if "on" in [token.text for token in chunk]]
gerundive_phrases = [chunk.text for chunk in doc.noun_chunks if "ing" in [token.text[-3:] for token in chunk]]
infinitive_clauses = [token.text for token in doc if token.dep_ == "xcomp"]
relative_clauses = [token.text for token in doc if token.dep_ == "relcl"]

# Print the identified phrases
print("\nPrepositional Phrases:", prepositional_phrases)
print("\nGerundive Phrases:", gerundive_phrases)
print("\nNon-finite clauses (Infinitive Clauses):", infinitive_clauses)
print("\nRelative Clauses:", relative_clauses)