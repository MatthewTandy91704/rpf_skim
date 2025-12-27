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

nlp = spacy.load("en_core_web_md")

doc = nlp("This is a sentence.")

print(nlp.pipe_names)
print(nlp.pipeline)

# custom pipeline components can be added to auto call a funct when nlp is called
# add own metadata to docs and tokens

from spacy.language import Language

@Language.component("custom_component")

def custom_component_function(doc):
    # do something to the doc here
    return doc

nlp.add_pipe("custom_component")

nlp = spacy.load("en_core_web_sm")

@Language.component("custom")
def custom_function(doc):
    print("Doc length:", len(doc))
    return doc

nlp.add_pipe("custom", first=True)

print("Pipeline:", nlp.pipe_names)

doc = nlp("Hello world")

# we can solve the problem of computing values based on tokens and their attributes
# as well as adding named entities, for example based on a dictionary
# by adding custom pipeline components
