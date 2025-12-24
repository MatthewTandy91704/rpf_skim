import spacy

from spacy.tokens import Doc, Span

from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print(doc1.similarity(doc2))

print(doc2.similarity(doc1))
