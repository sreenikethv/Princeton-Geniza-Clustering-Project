#@title Document search

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
