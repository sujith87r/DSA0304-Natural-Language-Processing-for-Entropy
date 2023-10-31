import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the input sentence
sentence = "book that flight"

# Process the sentence with spaCy
doc = nlp(sentence)

# Extract subcategorization frames
subcat_frames = {}

for token in doc:
    if token.dep_ == "dobj":  # Check for a direct object
        verb = token.head.text
        obj = token.text

        if verb not in subcat_frames:
            subcat_frames[verb] = []

        subcat_frames[verb].append(obj)

# Print the subcategorization frames
for verb, objects in subcat_frames.items():
    print(f"{verb} {', '.join(objects)}")
