def find(wordlist):
    length = 0
    for item in wordlist:
        if len(item) > length:
            length = len(item)
            temp = item
    return temp, length


GetInput = input("enter list of word: ")
Word = list(GetInput.split())
print(find(Word))


