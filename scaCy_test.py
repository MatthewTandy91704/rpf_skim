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