#@title

# to do:
# preprocess by opening google sheets or filter out ZeroType cells
# deal with any csv, not just those that are pgpid-type-tag-description
# filter out common phrases like (Information from Goitein's index cards)

#### Now that you've loaded in the dials above, load in the data from the .csv file by clicking the play button below.

import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_distances
import numpy as np

import dials

# Load data from csv file
with open('geniza_demo.csv', 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Read the header row
    pgpid_index = None
    description_index = None
    # Find the positions of "pgpid" and "description" in the header row
    for i, header in enumerate(header_row):
        if header.lower() == "pgpid":
            pgpid_index = i
        elif header.lower() == "description":
            description_index = i

    '''
    # Load data from csv file
    with open('geniza_demo.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        pgpids = []
        descriptions = []
        for row in reader:
            if len(row) >= 4:
                pgpids.append(row[0])
                descriptions.append(row[3])

    '''

    '''
        # Print the positions if found
        if pgpid_index is not None:
            print(f"Position of 'pgpid' is {pgpid_index}")
        else:
            print("Header 'pgpid' not found")
        if description_index is not None:
            print(f"Position of 'description' is {description_index}")
        else:
            print("Header 'description' not found")
    '''

    pgpids = []
    descriptions = []
    for row in reader:
      pgpids.append(row[pgpid_index])
      descriptions.append(row[description_index])

# Vectorize with TfidfVectorizer based on [descriptions]
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(descriptions)

# Find most common phrases
count_vectorizer = CountVectorizer(stop_words='english', ngram_range=(2,2)) #preprocess to extract all bigrams
count_matrix = count_vectorizer.fit_transform(descriptions)
phrase_frequencies = np.asarray(count_matrix.sum(axis=0)).ravel()
phrase_indices = np.argsort(phrase_frequencies)[::-1]
common_phrases = []
for index in phrase_indices:
    phrase = list(count_vectorizer.vocabulary_.keys())[list(count_vectorizer.vocabulary_.values()).index(index)]
    if phrase not in vectorizer.stop_words_:
        common_phrases.append(phrase)
    if len(common_phrases) == 5:
        break

# Remove most common phrases
for phrase in common_phrases:
    if phrase in vectorizer.vocabulary_:
        del vectorizer.vocabulary_[phrase]

# Re-vectorize with the updated vocabulary
X = vectorizer.fit_transform(descriptions)

# Calculate cosine distances between documents
distances = cosine_distances(X)
