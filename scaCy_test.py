import spacy

nlp = spacy.blank("en")
doc = nlp("I have a cat")

# Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

import spacy

nlp = spacy.blank("en")
doc = nlp("David Bowie is a PERSON")

# Look up the hash for the string label "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Look up the person_hash to get the string
person_string = nlp.vocab.strings[person_hash]
print(person_string)

from spacy.tokens import Doc, Span

words = ["Hello", "world", "!"]
spaces = [True, False, False]

doc = Doc(nlp.vocab, words = words, spaces = spaces)

span = Span(doc, 0, 2)

span_with_label = Span(doc, 0, 2, label="GREETING")

doc.ents = [span_with_label]

