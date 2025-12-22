import spacy

from spacy.tokens import Doc, Span

from spacy.matcher import Matcher


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
matcher = Matcher(nlp.vocab)

doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print(doc1.similarity(doc2))

print(doc2.similarity(doc1))

pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Add the pattern to the matcher and apply the matcher to the doc
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# testing for actual use case using an old message from Sol as my nlp
# this leads to a full proof of concept for at least the factor of picking out distancing
# in fact distancing would be very easy

test = nlp("Umeko’s expression shifted in confusion underneath her mask as she caught her balance and adjusted to the new environment. She disliked the small fighting space, much preferring open spaces, but oh well, she can manage. The barrier was impressive as well, in her mind, as someone who hasn’t had much experience with them at all. She skipped backwards to create 10 meters between them total, being careful to avoid the various pockets of lava as her hands flowed through signs swiftly. It just so happened that she needed practice with water release anyways. An orb of water formed in front of her, from which 7 sharp whips shot out at Dixue from the orb, appearing to aim straight for her abdomen, but 4 of the whips suddenly shifted its trajectory and bent in odd ways that led to one aiming for her left leg, one to her right arm, one to her neck, and the last seemingly going up and past her head. If she wasn’t careful, that last whip would bend again and snap at her back. They were fully capable of cutting through her armor, and deep into her skin due to the strength of this particular technique and Umeko’s control over her chakra allowing her to pinpoint those locations with dangerous sharpness")

distancing_pattern = [{"IS_DIGIT": True}, {"TEXT": "meters"}]
matcher.add("METER_PLURAL_PATTERN", [distancing_pattern])
matches = matcher(test)

distancing_pattern = [{"IS_DIGIT": True}, {"TEXT": "m"}]
matcher.add("METER_ABV_PATTERN", [distancing_pattern])
matches = matcher(test)

distancing_pattern = [{"IS_DIGIT": True}, {"TEXT": "meter"}]
matcher.add("METER_SINGULAR_PATTERN", [distancing_pattern])
matches = matcher(test)

print("Total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", test[start:end].text)
