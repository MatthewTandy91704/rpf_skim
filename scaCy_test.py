import spacy

from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"IS_DIGIT": True},
           {"LOWER": "fifa"},
           {"LOWER": "world"},
           {"LOWER": "cup"},
           {"IS_PUNCT": True}
           ]

doc = nlp("2018 FIFA World Cup: France won!")

pattern = [
    {"LEMMA": "love"}, {"POS": "VERB"}, {"POS": "NOUN"}
]

doc = nlp("I loved dogs but not I love cats more.")

pattern = [{"LEMMA": "buy"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}]

doc = nlp("I bought a smartphone. Now I'm buying apps.")

import spacy

# Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])