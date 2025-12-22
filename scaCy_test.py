import spacy

from spacy.tokens import Doc, Span


nlp = spacy.blank("en")

doc = nlp("It costs $5.")

print("Index: ", [token.i for token in doc])
print("Text: ", [token.text for token in doc])

print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# Write a pattern that matches a form of "download" plus proper noun
pattern = [{"LEMMA": "download"}, {"POS": "PROPN"}]

nlp = spacy.load("en_core_web_md")

doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print(doc1.similarity(doc2))

print(doc2.similarity(doc1))


test = nlp("meter")
