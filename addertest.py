#!/usr/bin/env python
#test script for libbaltcalc's addition function.
import libbaltcalc
import math
def atest(nA, nB):
	print ("(" + nA + ")+(" + nB + ")=(" + (libbaltcalc.btadd(nA, nB)) + ")")
	
atest("-", "-")
atest("-", "+")
atest("-", "0")
atest("+", "+")
atest("+", "-")
atest("+", "0")
atest("0", "0")
atest("0", "+")
atest("0", "-")
atest("------------", "++++++++++++")
atest("-0+", "+0-")
atest("--0+", "-+0-")
atest("-0-+", "+0+-")
# a chain adder to count to decimal 10 in both balanced ternary and decimal.
def btest(decnumtocountto):
	decicnt=0
	prevbtnum="0"
	print("actual decimal count| BT count in decimal | BT count")
	while decicnt!=decnumtocountto:
		
		print (str(decicnt) + "|" +  str(libbaltcalc.BTTODEC(prevbtnum)) + "|" +  prevbtnum)
		prevbtnum=(libbaltcalc.btadd(prevbtnum, "+"))
		decicnt += 1
		
def ctest(decnumtocountto):
	decicnt=0
	dicecnt=1
	prevbtnum="0"
	print("actual decimal count| BT count in decimal | BT count")
	while dicecnt!=decnumtocountto:
		
		print (str(decicnt) + "|" +  str(libbaltcalc.BTTODEC(prevbtnum)) + "|" +  prevbtnum)
		prevbtnum=(libbaltcalc.btadd(prevbtnum, "-"))
		decicnt -= 1
		dicecnt -= 1

btest(10001)
ctest(-10)

#small test of the decinal to balanced ternary converter
numA=(10000)
print(numA)
print(libbaltcalc.DECTOBT(numA))
print(libbaltcalc.BTTODEC(libbaltcalc.DECTOBT(numA)))



