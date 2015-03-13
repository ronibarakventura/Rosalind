s = ##insert string

ss = s.split()

words = []
count = []

for i in ss:
    if i in words:
        count[words.index(i)] = count[words.index(i)] + 1
        
    else:
        words.append(i)
        count.append(1)
        

for j in words:
    print j, count[words.index(j)]