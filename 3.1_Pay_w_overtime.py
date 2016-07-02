# Coursera Python for informatics,  Getting Started
# Assignment 3.1
# Nathan Richardson
# July 2, 2016

hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = float(raw_input("enter rate:"))
overtime = 0                      
if h > 40:
	overtime = h - 40
	h = 40
    
orate = rate * 1.5

pay = h*rate + overtime*orate

print pay
