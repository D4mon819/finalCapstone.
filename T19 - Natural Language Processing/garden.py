import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Created in a list called gardenpathSentences
gardenpathSentences = [

    "I convinced her children are noisy.",
    "The horse raced past the barn fell.",
    "That Jill is never here hurts.",
    "Mary gave the child a Band-Aid.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("\nSentence:", sentence)
    for token in doc:
        print(token.text, token.pos_, token.dep_)
    for ent in doc.ents:
        print(ent.text, ent.label_, spacy.explain(ent.label_))

# Comment about two entities that were looked up
# 1. "Jill" (PERSON): The entity 'Jill' is recognized as a person. This makes sense as Jill is a common personal name.
# 2. "Band-Aid" (PRODUCT): The entity 'Band-Aid' is recognized as a product. This also makes sense as Band-Aid is a well-known brand of adhesive bandages.
