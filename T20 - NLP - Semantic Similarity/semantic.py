import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("car")
word5 = nlp("bicycle")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word4.similarity(word5))

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))

#   "Cat" and "monkey" are more similar to each other compared to "banana."
#   Since cats and monkeys are both animals, whereas a banana is a fruit,
#   so the semantic similarity between "cat" and "monkey" is higher than between either of them and "banana."

#   As for my example "car" and "bicycle", These two words might have a lower similarity score .
#   Its because they are both modes of transportation but differ significantly in terms of size, shape, and other attributes.

#   As the difference between 'en_core_web_md' and 'en_core_web_sm,'
#   'en_core_web_md' is a medium-sized model that includes word vectors, allowing for more accurate similarity calculations.
#   'en_core_web_sm' is a smaller model without word vectors, so its similarity calculations might not be as precise.
#   The smaller model may also have a smaller vocabulary, leading to potentially different results, especially for less common words or phrases.