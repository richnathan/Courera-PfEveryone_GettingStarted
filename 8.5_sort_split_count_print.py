#input = raw_input("please enter file name : ")
input = 'mbox-short.txt'
try:
    file = open(input)
except:
    print 'cant open file:' , input
    exit()
total = []
count = 0
for word in file:
    word = word.rstrip()
    words = word.split()
    if words == [] : continue
    if words[0] != 'From' : continue
    print words[1]
    count = count + 1
   
print 'There were', count, "lines in the file with From as the first word"
#print sorted(total)
