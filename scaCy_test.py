import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

print(coffee_hash)
print(coffee_string)

doc = nlp("I love coffee")

lexeme = nlp.vocab["coffee"]

print(lexeme.text, lexeme.orth, lexeme.is_alpha)

#lexeme = entry in the vocabulary
