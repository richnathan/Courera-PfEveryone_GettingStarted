#input = raw_input("please enter file name : ")
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
    counts[words[1]]=counts.get(words[1],0)+1

maxv = None
maxk = None
for k,v in counts.items():
	if maxv == None or maxv < v:
		maxv = v
		maxk = k

print maxk, maxv
