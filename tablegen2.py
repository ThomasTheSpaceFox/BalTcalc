#!/usr/bin/env python
#test script for libbaltcalc's addition function.
import libbaltcalc
import math

#padding table
def pad9(inpnum):
	padcnt=0
	for f in inpnum:
		padcnt +=1
	if padcnt==0:
		return("000000000" + inpnum)
	if padcnt==1:
		return("00000000" + inpnum)
	if padcnt==2:
		return("0000000" + inpnum)
	if padcnt==3:
		return("000000" + inpnum)
	if padcnt==4:
		return("00000" + inpnum)
	if padcnt==5:
		return("0000" + inpnum)
	if padcnt==6:
		return("000" + inpnum)
	if padcnt==7:
		return("00" + inpnum)
	if padcnt==8:
		return("0" + inpnum)
	if padcnt==9:
		return(inpnum)
		 

def btestpos(decnumtocountto):
	decicnt=0
	decnumtocountto += 1
	prevbtnum="0"
	print("actual decimal count| BT count in decimal | BT count")
	while decicnt!=decnumtocountto:
		
		print (pad9(prevbtnum))
		#print (str(decicnt) + "|" +  str(libbaltcalc.BTTODEC(prevbtnum)) + "|" +  prevbtnum)
		prevbtnum=(libbaltcalc.btadd(prevbtnum, "+"))
		decicnt += 1
def btestneg(decnumtocountto):
	decicnt=0
	decnumtocountto -= 1
	prevbtnum="0"
	print("actual decimal count| BT count in decimal | BT count")
	while decicnt!=decnumtocountto:
		
		print (pad9(prevbtnum))
		#print (str(decicnt) + "|" +  str(libbaltcalc.BTTODEC(prevbtnum)) + "|" +  prevbtnum)
		prevbtnum=(libbaltcalc.btadd(prevbtnum, "-"))
		decicnt -= 1
btestneg(-9841)
#print("000000000")
#btestpos(9841)
