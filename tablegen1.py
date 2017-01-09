#!/usr/bin/env python
#test script for libbaltcalc's addition function.
import libbaltcalc
#import math

def btest(decnumtocountto):
	decicnt=0
	decnumtocountto += 1
	prevbtnum="0"
	print("actual decimal count| BT count in decimal | BT count")
	while decicnt!=decnumtocountto:
		
		#print (prevbtnum)
		print (str(decicnt) + "|" +  str(libbaltcalc.BTTODEC(prevbtnum)) + "|" +  prevbtnum)
		prevbtnum=(libbaltcalc.btadd(prevbtnum, "+"))
		decicnt += 1
btest(2017)