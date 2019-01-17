import csv
import re
from langdetect import detect

def language(tweet):
    lang = detect(tweet)
    return lang

def linkRemoval(tweet):
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'https:\/\/.*', '', tweet)
    return tweet

def csvClean(inputFile, outputFile):
    r = csv.reader(open(inputFile))
    entry = list(r)
    newEntry = []
    for i in range(len(entry)):
        try:
            lang = language(entry[i][1])
            if lang =='en':
                entry[i][1] = linkRemoval(entry[i][1])
                newEntry.append(entry[i])
        except:
            print("Exception occurred in language detection. Considering tweet as invalid")
    w = csv.writer(open(outputFile, 'w'))
    w.writerows(newEntry)

if __name__ == "__init__":
    main()