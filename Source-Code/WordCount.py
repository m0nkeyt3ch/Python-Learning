source = "H:\\GitHub\\Python-Learning\\Source-Code\\text.txt"
file = open(source, "r")
wordcount = {} #dictionary
for word in file.read().split():
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('?', '')
    word = word.replace('"', '')
    if word.lower() not in wordcount:
        wordcount[word.lower()] = 1
    else:
        wordcount[word.lower()] += 1
for sentence in wordcount.items():
    print("{}\t{}".format(*sentence))