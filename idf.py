import csv

def dfdict(inputFile):
    r = csv.reader(open(inputFile))
    entry = list(r)
    worddict = {}
    for i in range(len(entry)-1):
        l = list(entry[i+1][4].split("|"))
        for word in l:
            if word in worddict:
                worddict[word] = worddict[word] + 1
            else:
                worddict[word] = 1
    return worddict

if __name__ == "__init__":
    main()