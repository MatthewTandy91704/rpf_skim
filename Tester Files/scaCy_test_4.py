# when nlp is called
#                               nlp
# Text -> {tokenizer -> tagger -> parser -> ner -> ...} -> Doc
#  name  -     description       -    creates
# tagger - part-of-speech tagger - Token.tag, Token.pos
# parser - dependency parser - Token.dep, Token.head, Doc.sents, Doc.noun_chunks
# ner - named entity recognizer - Doc.ents, Token.ent_iob, Token.ent_type
# textcat - text classifier - Doc.cats

# pipeline defined in spaCy model's config.cfg in order - is it possible to change this order? Would there be any benefits to doing this?
# the built in components need binary data to make predictions - how would i appropriately create more binary data?

import spacy

from spacy.matcher import Matcher

nlp = spacy.blank("en")

doc = nlp("This is a sentence.")

print(nlp.pipe_names)
print(nlp.pipeline)
