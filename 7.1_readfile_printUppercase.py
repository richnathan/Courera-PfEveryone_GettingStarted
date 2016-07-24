# Use words.txt as the file name
input = raw_input("please enter file name : ")

try:
    file = open(input)
except:
    print 'cant open file:' , input
    exit()
count = 0
for line in file:
    line = line.rstrip()
    print line.upper()
    count = count +1
