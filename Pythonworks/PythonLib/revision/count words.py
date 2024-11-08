x="Hi All We are going for a trip"
wordcount=1
for i in range(len(x)):
    if (x[i]== ' ' or x=='\n' or x=='\t'):
        wordcount+=1
print(wordcount)