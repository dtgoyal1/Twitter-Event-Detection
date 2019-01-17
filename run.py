import cleanup
import csv
import preproc
import idf
import tfidfsimilarity

inputF = input('Enter dataset file name : ')
outputF = input('Enter name of cleaned up file : ')
finalF = input('Enter name of file with features : ')
r = csv.reader(open(inputF))
entry = list(r)
count = 0
for i in range(1,len(entry)):
    count = count + len(entry[i][1])
print('The average number of characters per tweet is ' + str((count/(len(entry)-1))))
print('Cleaning dataset. Please wait ... ')
cleanup.csvClean(inputF,outputF)
r = csv.reader(open(outputF))
entry = list(r)
count = 0
for i in range(1,len(entry)):
    count = count + len(entry[i][1])
print('After cleanup, the average number of characters per tweet is ' + str((count/(len(entry)-1))))
print('Extracting features ... ')
preproc.extractFeatures(outputF,finalF)
fredict = idf.dfdict(finalF)
count = 0
for key,val in fredict.items():
    count = count + val
print('The average number of features per tweet is ' + str((count/len(fredict))))
r = csv.reader(open(finalF))
entry = list(r)
print('Lets find the cosine similarity between two tweets.')
tweet1 = int(input('Enter tweet ID of 1st tweet : '))
tweet2 = int(input('Enter tweet ID of 2nd tweet : '))
m,n = tfidfsimilarity.tfidf(list(entry[tweet1][4].split("|")), list(entry[tweet2][4].split("|")), fredict)
sim = tfidfsimilarity.similar(m,n)
print('The similarity measure between tweet '+str(tweet1)+' and tweet '+str(tweet2)+' is '+str(sim))