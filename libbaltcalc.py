#!/usr/bin/env python
import math
#HELPTEXT = ('''commands:
#BTTODEC: convert a number into balancet
#''')
# syntax info:
#trit order is least signifigant digit on right
#1=+
#0=0
#T=-

def numflip(numtoflip):
	return(numtoflip[::-1])
#converts balanced ternary numbers to decimal.
def BTTODEC(NUMTOCONV1):
	FLIPPEDSTR1=(numflip(NUMTOCONV1))
	EXTRAP1=0
	SUMDEC1=0
	for btnumlst1 in FLIPPEDSTR1:
		EXTPOLL1 = (3**EXTRAP1)
		if btnumlst1==("+"):
			SUMDEC1 += EXTPOLL1
		if btnumlst1==("-"):
			SUMDEC1 -= EXTPOLL1
		EXTRAP1 += 1
	return (SUMDEC1)

#inverts the positive and negative numerals in a balanced ternary number, 
#(ie 1T0T would become T101 and vice versa)
def BTINVERT(numtoinvert):
	BTINV1 = numtoinvert.replace("-", "P").replace("+", "-").replace("P", "+")
	#print BTINV2
	return (BTINV1)



#prodotype addition function.
#eventually will add longer balanced ternary numbers.
def btadd(numA, numB):
	#check to ensure any final carries are preformed.
	numA=("0" + numA)
	numB=("0" + numB)
	numA=(numflip(numA))
	numB=(numflip(numB))
	numAcnt=0
	numBcnt=0
	curregA=1
	curregB=1
	carry="0"
	resbatch=""
	for anA in numA:
		numAcnt += 1
	for anB in numB:
		numBcnt += 1
	if (numAcnt > numBcnt):
		forlist = numA
	if (numAcnt < numBcnt):
		forlist = numB
	if (numAcnt==numBcnt):
		forlist = numA
	for dxpink in forlist:
		loopregA=1
		loopregB=1
		for Areg in numA:
			
			if curregA==loopregA:
				returnedA=1
				Aval = Areg
				break
			loopregA += 1
		for Breg in numB:
			
			if curregB==loopregB:
				returnedB=1
				Bval = Breg
				break
			loopregB += 1
		#print ("A:" + Aval + str(returnedA))
		#print ("B:" + Bval + str(returnedB))
		#Aval=+ rules:
		if (Aval=="+" and Bval=="+"):
			if carry=="0":
				resbatch = ("-" + resbatch)
				carry="+"
			elif carry=="+":
				resbatch = ("0" + resbatch)
				carry="+"
			elif carry=="-":
				resbatch = ("+" + resbatch)
				carry="0"
		elif (Aval=="+" and Bval=="0"):
			if carry=="0":
				resbatch = ("+" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("-" + resbatch)
				carry="+"
			elif carry=="-":
				resbatch = ("0" + resbatch)
				carry="0"
		elif (Aval=="+" and Bval=="-"):
			if carry=="0":
				resbatch = ("0" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("+" + resbatch)
				carry="0"
			elif carry=="-":
				resbatch = ("-" + resbatch)
				carry="0"
		#Aval=- rules
		elif (Aval=="-" and Bval=="-"):
			if carry=="0":
				resbatch = ("+" + resbatch)
				carry="-"
			elif carry=="-":
				resbatch = ("0" + resbatch)
				carry="-"
			elif carry=="+":
				resbatch = ("-" + resbatch)
				carry="0"
		elif (Aval=="-" and Bval=="0"):
			if carry=="0":
				resbatch = ("-" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("0" + resbatch)
				carry="0"
			elif carry=="-":
				resbatch = ("+" + resbatch)
				carry="-"
		elif (Aval=="-" and Bval=="+"):
			if carry=="0":
				resbatch = ("0" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("+" + resbatch)
				carry="0"
			elif carry=="-":
				resbatch = ("-" + resbatch)
				carry="0"
		#Aval=0 rules
		elif (Aval=="0" and Bval=="0"):
			if carry=="0":
				resbatch = ("0" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("+" + resbatch)
				carry="0"
			elif carry=="-":
				resbatch = ("-" + resbatch)
				carry="0"
		elif (Aval=="0" and Bval=="-"):
			if carry=="0":
				resbatch = ("-" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("0" + resbatch)
				carry="0"
			elif carry=="-":
				resbatch = ("+" + resbatch)
				carry="-"
		elif (Aval=="0" and Bval=="+"):
			if carry=="0":
				resbatch = ("+" + resbatch)
				carry="0"
			elif carry=="+":
				resbatch = ("-" + resbatch)
				carry="+"
			elif carry=="-":
				resbatch = ("0" + resbatch)
				carry="0"
		curregA += 1
		curregB += 1
		Aval="0"
		Bval="0"
		returnedA=0
		returnedB=0
	return (resbatch)
	


#gets a balanced ternary number from the user an parses it based on various 
#balanced ternary notation conventions. currently only the 1,0,T and +,0,- conventions.
def BTstrgetsort():
	NUMPARS = raw_input('>:')
	NUMPARS = NUMPARS.replace("1", "+").replace("T", "-")
	return (NUMPARS)
#gets a sigle-trit balanced ternary number from the user an parses it based on various 
#balanced ternary notation conventions. currently only the 1,0,T and +,0,- conventions.
def BTstrgetsingle():
	NUMPX = BTstrgetsort()
	for fstdig in NUMPX:
		return (fstdig)

# a "programmable" biased and gate. returns a positive if:
#input a (inpA) = input b (inpB) = polarity line (polarset)
#else it returns zero
def progbiasand(polarset, inpA, inpB):
	if (inpA==polarset and inpB==polarset):
		return("+")
	elif (inpA!=polarset or inpB!=polarset):
		return("0")
#a polarized and gate
#returns + if both input A (inpA) and input B (inpB) = + 
#returns - if both input A (inpA) and input B (inpB) = -
#otherwise it returns zero
def polarityand(inpA, inpB):
	if (inpA=="+" and inpB=="+"):
		return("+")
	elif (inpA=="-" and inpB=="-"):
		return("-")
	elif (inpA!="+" or inpB!="+"):
		return("0")
	elif (inpA!="-" or inpB!="-"):
		return("0")

# a programmable biased or gate returns "+" if either or both inputs equal the pollarity line (polarset)
#else it returns "0"
def progbiasor(polarset, inpA, inpB):
	if (inpA==polarset or inpB==polarset):
		return("+")
	elif (inpA!=polarset or inpB!=polarset):
		return("0")
# a programmable biased orn gate returns "+" if either  equal the pollarity line (polarset)
#returns "0" either if neither or both inputs equal the pollarity line (polarset)
def progbiasnor(polarset, inpA, inpB):
	if (inpA==polarset and inpB==polarset):
		return("0")
	elif (inpA!=polarset and inpB==polarset):
		return("+")
	elif (inpA==polarset and inpB!=polarset):
		return("+")
	elif (inpA!=polarset and inpB!=polarset):
		return("0")

