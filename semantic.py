import spacy
nlp = spacy.load('en_core_web_md')

print("\t*Compulsory Task 1*")
print("")
# Create a file called semantic.py and run all the code extracts above (I assume you meant SE T38 pdf document).
# Question - Write a note about what you found interesting about the similarities between cat, monkey and banana.
# Answer - Similarity between words seem to be based on information describing the nature and characteristics of the
#          object. Monkey-banana have some similarity since monkeys eat banana. Monkey-cat has a higher similarity value
#          since they're both animals (mammals) so perhaps the category both objects belong to have higher significance.
#          Cat-banana have very low similarity since cats don't usually consume bananas so there is little to no
#          transitive relationship between them.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("")
print("\t*Example of my own*")
word4 = nlp("moon")
word5 = nlp("rocket")
word6 = nlp("satellite")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# -------------- #
print("")
print("\t*Code from SE T38 pdf document - compare a series of words*")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# ---------------- #
print("")
print("\t*Code from SE T38 pdf document - comparing sentences*")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go", "Hello, there is my car",
"I\'ve lost my car in my car", "I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
