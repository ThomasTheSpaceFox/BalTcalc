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


#converts balanced ternary numbers to decimal.
def BTTODEC(NUMTOCONV1):
	FLIPPEDSTR1=(NUMTOCONV1[::-1])
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

