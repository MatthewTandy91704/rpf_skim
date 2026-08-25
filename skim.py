import spacy

from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")
matcher = Matcher(nlp.vocab)

test = nlp("Umeko’s expression shifted in confusion underneath her mask as she caught her balance and adjusted to the new environment. She disliked the small fighting space, much preferring open spaces, but oh well, she can manage. The barrier was impressive as well, in her mind, as someone who hasn’t had much experience with them at all. She skipped backwards to create 10 meters between them total, being careful to avoid the various pockets of lava as her hands flowed through signs swiftly. It just so happened that she needed practice with water release anyways. An orb of water formed in front of her, from which 7 sharp whips shot out at Dixue from the orb, appearing to aim straight for her abdomen, but 4 of the whips suddenly shifted its trajectory and bent in odd ways that led to one aiming for her left leg, one to her right arm, one to her neck, and the last seemingly going up and past her head. If she wasn’t careful, that last whip would bend again and snap at her back. They were fully capable of cutting through her armor, and deep into her skin due to the strength of this particular technique and Umeko’s control over her chakra allowing her to pinpoint those locations with dangerous sharpness")

distancing_pattern = [
    {"LIKE_NUM": True},
    {"LOWER": {"IN": ["meters", "meter", "m", # base unit: meter
                      "feet", "foot", "ft", # base unit: foot
                      "inches", "inch", "in" # base unit: inch
    ]}}
]

positioning_pattern = [
    [
        {"LOWER": "behind"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "above"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "below"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "underneath"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "beside"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "next"},
        {"LOWER": "to"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ],
    [
        {"LOWER": "in"},
        {"LOWER": "front"},
        {"LOWER": "of"},
        {"LOWER": {"IN": ["him", "her", "them", "it"]}}
    ]
]

movement_pattern = [
    {"LOWER": {"IN": ["sprint", "sprints", "sprinted",
                      "skip", "skips", "skipped",
                      "run", "runs", "ran",
                      "walk", "walks", "walked",
                      "slide", "slides", "slid"
                      "float", "floats", "floated",
                      "fly", "flies", "flew",
                      "dig", "digs", "dug",
                      "swim", "swims", "swam",
                      "jump", "jumps", "jumped"]}},
]

matcher.add("DISTANCE", [distancing_pattern])
matcher.add("POSITION", positioning_pattern)
matcher.add("MOVEMENT", [movement_pattern])
matches = matcher(test)
print("Total matches found:", len(matches))
for match_id, start, end in matches:
    print("Match found:", test[start:end].text)
