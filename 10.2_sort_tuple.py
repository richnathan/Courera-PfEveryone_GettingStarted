input = 'mbox-short.txt'
try:
    file = open(input)
except:
    print 'cant open file:' , input
    exit()

counts = dict()

for word in file:
    word = word.rstrip()
    words = word.split()
    if words == [] : continue
    if words[0] != 'From' : continue
    yup = words[5]
    yup2 = yup[0:2]
    #print yup2
    counts[yup2]=counts.get(yup2,0)+1
    #counts[words[5]]=counts.get(words[5],0)+1
    #print counts

    
#print counts
dude = list()
for k,v in counts.items():
	j= k[0:2]
	dude.append((j,v))
	#print j,v
    
    
    
dude.sort()
#print dude 
for k,v in dude:
	print k,v
