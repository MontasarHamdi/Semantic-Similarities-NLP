import spacy

nlp = spacy.load("en_core_web_md")

# Creating an empty dictionary
movie_dict = {}

# Reading file
movie_txt = open("movies.txt").read()
my_movie = movie_txt.split('\n')
my_movie.pop()
# Saving contents of file in a dictionary
for i in my_movie:
    movie_dict[i.split(":")[0]] = i.split(":")[1]  # Split movie letter from movie description when running comparison.


similarity_value = []  # Create another empty diction to store similarity values
for i in movie_dict.values():
    sentence_to_compare = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
     the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
     Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator'''

    model_sentences = nlp(sentence_to_compare)

    # Comparing each movie description with the given description and append values to similarity_value list
    similarity = nlp(i).similarity(model_sentences)
    print("Description of movie: " + i + ":" + "\nSimilarity value: " + str(similarity) + "\n")
    similarity_value.append(similarity)

movie_title = []  # Empty list for movie titles and append the key of each value to list
for i in movie_dict.keys():
    movie_title.append(i)

# Print the movie title
print("Movie user should watch based on similarity: " + movie_title[similarity_value.index(max(similarity_value))])
