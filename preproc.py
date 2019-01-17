import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import tfidfsimilarity
from autocorrect import spell

stop_words = set(stopwords.words('english'))

def stopword(tweet):
    tokens = word_tokenize(tweet)
    newTokens = [token for token in tokens if not token in stop_words]
    return newTokens

def postag(tweet):
    tokens = stopword(tweet)
    posTokens = nltk.pos_tag(tokens)
    return posTokens

def extractFeatures(inputFile, outputFile):
    r = csv.reader(open(inputFile))
    entry = list(r)
    entry[0].append('features')
    j = 1
    ps = PorterStemmer()
    while j < len(entry):
        features = postag(entry[j][1])
        featureVector = []
        for f in features:
            if f[1] == 'NN' or f[1] == 'NNS' or f[1] == 'NNP' or f[1] == 'NNPS' or f[1] == 'VB' or f[1] == 'VBD' or f[1] == 'VBG' or f[1] == 'VBN' or f[1] == 'VBP' or f[1] == 'VBZ':
                if f[0].isalpha():
                    n = ps.stem(f[0])
                    featureVector.append(n) 
        entry[j].append(featureVector)
        s = ''
        for word in featureVector:
            s = s + "|" + word
        entry[j][4] = s[1:]
        j = j + 1
    writer = csv.writer(open(outputFile,'w'))
    writer.writerows(entry)


if __name__=="__init__":
    main()