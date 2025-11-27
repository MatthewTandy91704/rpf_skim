import spacy

from spacy.tokens import Doc, Span

nlp = spacy.load("en_core_web_md")

doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print(doc1.similarity(doc2))