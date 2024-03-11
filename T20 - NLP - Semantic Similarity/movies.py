import spacy

def next_movie(description):
    nlp = spacy.load('en_core_web_md')
    with open('movies.txt', 'r', encoding='utf') as file :
        movie_descriptions = file.readlines()

    max_similarity = -1
    most_similar_movie = ''


    for movie_description in movie_descriptions :
            similarity = nlp(movie_description.strip()).similarity(nlp(description))

    if similarity > max_similarity :
            max_similarity = similarity
            most_similar_movie = movie_description.strip()
    return most_similar_movie

description = ("""
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a 
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.
""")
movie_recommand = next_movie(description)
print("Next movie to watch:", movie_recommand)