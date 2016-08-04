#input = raw_input("please enter file name : ")
input = 'romeo.txt'
try:
    file = open(input)
except:
    print 'cant open file:' , input
    exit()
total = []
for word in file:
#    print word, "11"
    words = word.rstrip()
    words = word.split() 
#    print words, "000"
    for i in words:
        if i in total: 
            continue
        else:
    		total.append(i)
    
#    if line == words: continue
#    tline = sline.append(line)
#    tline.sort()
#    print sline
#print tline

print sorted(total)
