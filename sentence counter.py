from collections import Counter
sentence = 'Hippo runs to us'
counts=Counter(sentence) 
for i in sentence:
    print(i,counts[i])