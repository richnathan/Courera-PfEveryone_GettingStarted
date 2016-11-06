import re
total = 0
input = 'regex_sum_287792.txt'
try:
    file = open(input)
except:
    print 'cant open file:' , input
    exit()
for line in file:
    #print line
    x = "3453 hello world 12"
    y = re.findall('[0-9]+', line)
    if len(y) > 0:
        z = map(int, y)
        #print y, "y"
        #print z, "z"
        total = sum(z) + total

print total
#print "done"
file.close()
