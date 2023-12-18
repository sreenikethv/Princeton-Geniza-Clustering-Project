"""
Print neighbors for each document based on the provided data.

Parameters:
- pgpids: List of document IDs.
- descriptions: List of document descriptions.
- distances: 2D array of distances between documents.
- num_neighbors: Number of neighbors to display (default is 5).
- distance_threshold: Maximum distance to consider a neighbor (default is 0.1).
"""

import numpy as np

import dials
import load_csv.py

def print_all_neighbors(pgpids, descriptions, distances, num_neighbors=5, distance_threshold=0.1):
    for i in range(len(pgpids)):
        print("Neighbors for document", pgpids[i])
        print("Description:", descriptions[i], "\n")
        # Sort distances and get indices of closest neighbors
        closest = np.argsort(distances[i])[:num_neighbors+1]
        for j in closest:
            if (j != i and distances[i][j] >= distance_threshold):
                print("Document", pgpids[j], "with distance", distances[i][j])
                print(descriptions[j], "\n")
        print("------------------------------------\n")

def user_search()
    while True:
        number = input("Please enter a pgpid (or 'q' to quit): ")
        if number.lower() == 'q':
            break
        try:
          index = 0
          found = False
          for i in range(len(pgpids)):
            if pgpids[i] == number:
              index = i
              found = True
          if (found == False):
            raise ValueError("Invalid pgpid: {} not found in the pgpids list".format(number))
    
          print("Neighbors for document", pgpids[index], " ", 'https://geniza.princeton.edu/en/documents/' + pgpids[index] + '/')
          print("Description:", descriptions[index], "\n")
          #print('https://geniza.princeton.edu/en/documents/' + pgpids[index] + '/')
    
          closest = np.argsort(distances[index])[:num_neighbors+1]
          for j in closest:
              dist = distances[index][j]
              pgp = pgpids[j]
              if (j != index and dist >= distance_threshold):
                  if (dist > 0.90):
                    print('\033[92m' + 'Document ' + pgp + '\033[0m', " ",
                          'https://geniza.princeton.edu/en/documents/' + pgp + '/')
                    # print("Distance", pgp, "with distance", dist)
                  elif (dist > 0.80):
                    print('\033[33m' + 'Document ' + pgp + '\033[0m', " ",
                          'https://geniza.princeton.edu/en/documents/' + pgp + '/')
                  else:
                    print('\033[91m' + 'Document ' + pgp + '\033[0m', " ",
                          'https://geniza.princeton.edu/en/documents/' + pgp + '/')
                  print(descriptions[j], "\n")
          print("------------------------------------\n")
    
        except ValueError:
            print("Invalid input. Please enter a valid pgpid or 'q' to quit.\n")
