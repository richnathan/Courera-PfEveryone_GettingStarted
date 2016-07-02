# Coursera Python for informatics,  Getting Started
# Week 5 Assignment 3.3
# Nathan Richardson
# July 2, 2016

score = float(raw_input("Enter Score between 0.0 and 1.0: "))

if score > 1:
	score = float(raw_input("Enter Score between 0.0 and 1.0 "))

elif score < 0:
		score = float(raw_input("Enter Score between 0.0 and 1.0 "))
    
else:    
    if score >= 0.9:
        grade= 'A'
    elif score >=0.8:
        grade= 'B'
    elif score >=0.7:
        grade= 'C'
    elif score >=0.6:
        grade= 'D'
    else :
        score >=0.5
        grade= 'F'
    print grade
