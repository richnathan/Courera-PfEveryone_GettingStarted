text = "X-DSPAM-Confidence:    0.8475"
yup = text.find('0')
dude = len(text)
yup2 = text.find('5',23)
yup3 = float(text[yup:dude])
#print yup
#print yup2
#print dude
print yup3
