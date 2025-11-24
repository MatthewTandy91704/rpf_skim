import spacy

nlp = spacy.blank("en")

doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are.")

for token in doc:

    if token.is_alpha:
        next_token = doc[token.i + 1]

        if next_token.text == "%":
            print("Percentage found:", token.text)