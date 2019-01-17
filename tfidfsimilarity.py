import csv
import idf
import math

fredict = idf.dfdict('datafeatures.csv')

def tf(word, tweet):
    count = 0
    for feature in tweet:
        if feature == word:
            count = count + 1
    return count

def tfidf(tweet1, tweet2, fredict):
    tweets=[]
    for word in tweet1 + tweet2:
        if not word in tweets:
            tweets.append(word)
    m=[]
    n=[]
    for word in tweets:
        tf1 = tf(word,tweet1)
        tf2 = tf(word,tweet2)
        idf = math.log10(len(fredict)/fredict[word])
        m.append(tf1*idf)
        n.append(tf2*idf)
    print(m)
    print(n)
    return m,n

def similar(m,n):
    num = sum(val1*val2 for val1,val2 in zip(m,n))
    den1 = sum(val**2 for val in m)
    den2 = sum(val**2 for val in n)
    return num/(math.sqrt(den1)*math.sqrt(den2))

if __name__=="__init__":
    main()