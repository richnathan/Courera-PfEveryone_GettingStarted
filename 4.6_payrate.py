#print "how many hours per week?"
try:
    hours=float(raw_input("how many hours per week?"))
except:
#    print 'numbers only please'
#    print "how many hours per week?"
    hours=float(raw_input("numbers only please, how many hours per week?"))
#print "hours", hours
#print "pay rate?"
rate=float(raw_input("pay rate?"))
def computepay(hours, rate):
    if hours >40:
#        print 'thats a lot of hours bro!'
        overtime = float( (hours-40) * 1.5)*rate
        hours = 40
#        print 'overtime $',overtime
    else:
        overtime =0
    
    pay =hours*rate + overtime
 #   print "pay $",pay
    return pay

i = computepay(hours,rate)
print i
