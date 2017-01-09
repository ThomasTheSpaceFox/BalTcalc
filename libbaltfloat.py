import math
#import libbaltcalc

#please note: This Library is NOT YET WORKING CORRECTLY.

#prototype floating point library.

#this took a bit of work.

#not the simplest thing to do. 

#definately more complex than integers :p

#and will someone please fix the mess of a decimal to balanced ternary
#float conversion function. >.<

def numflip(numtoflip):
	return(numtoflip[::-1])
	
#returns first part of a balanced ternary float.
def uprad(NUMTOPROC):
	radcnt=1
	for radpic in (NUMTOPROC.split('.')):
		if radcnt==(1):
			return(radpic)
		radcnt += 1
	return
	
def downrad(NUMTOPROC):
	radcnt=1
	for radpic in (NUMTOPROC.split('.')):
		if radcnt==(2):
			return(radpic)
		radcnt += 1
	return

def radmerge(uprd, downrd):
	return(uprd + "." + downrd)

#this complicated function converts Balanced Ternary 
#Floats to Decimal floats. :p
#if the input number is not a float, it acts like the libbaltcalc equiv.
def BTTODEC(NUMTOCONV1):
	FLIPPEDSTR2=""
	FLIPPEDSTR1=(numflip(uprad(NUMTOCONV1)))
	FLIPPEDSTR2=(downrad(NUMTOCONV1))
	if FLIPPEDSTR2 is None:
		NULLBAR2=1
	else:
		NULLBAR2=0
	#for f in FLIPPEDSTR2:
	#	print f
	EXTRAP1=0
	SUMDEC1=0
	EXTRAP2=-1
	for btnumlst1 in FLIPPEDSTR1:
		EXTPOLL1 = (3**EXTRAP1)
		if btnumlst1==("+"):
			SUMDEC1 += EXTPOLL1
		if btnumlst1==("-"):
			SUMDEC1 -= EXTPOLL1
		EXTRAP1 += 1
	#print SUMDEC1
	if NULLBAR2==0:
		
		for btnumlst2 in FLIPPEDSTR2:
			#print btnumlst2
			EXTPOLL2 = (3**EXTRAP2)
			#print "foo"
			#print EXTPOLL2
			#EXTPOLL2=(float("0." + str(EXTPOLL2)))
			
			if btnumlst2==("+"):
				SUMDEC1 += EXTPOLL2
			if btnumlst2==("-"):
				SUMDEC1 -= EXTPOLL2
			#print ("foo>" + str(SUMDEC1))
			EXTRAP2 -= 1
	#print SUMDEC1
	SUMDECMAIN=(SUMDEC1)
	return (SUMDECMAIN)

#this complicated function converts Decimal
#Floats to Balanced Ternary floats. :p
#if teh input number is not a float, it acts like the libbaltcalc equiv.
#BROKEN!!!!! (SEE BELOW)
def DECTOBT(NUMTOCONVB):
	digbat=""
	digbat2=""
	NUMTOCONV1=int(uprad(str(NUMTOCONVB)))
	PRETEST1=(downrad(str(NUMTOCONVB)))
	if PRETEST1 is None:
		NULLBAR=1
		#print "WHO"
	else:
		NULLBAR=0
		NUMTOCONV2=int(downrad(str(NUMTOCONVB)))
		#print NUMTOCONV2
	while NUMTOCONV1 != 0:
		if NUMTOCONV1 % 3 == 0:
			#note_digit(0)
			digbat=("0" + digbat)
		elif NUMTOCONV1 % 3 == 1:
			#note_digit(1)
			digbat=("+" + digbat)
		elif NUMTOCONV1 % 3 == 2:
			#note_digit(-1)
			digbat=("-" + digbat)
		NUMTOCONV1 = (NUMTOCONV1 + 1) // 3
	if digbat=="":
		digbat="0"
	#this section is Broken!!!!!!!!!!
	#pls fix this. 0.+-- is not even close to 0.5 XD
	if NULLBAR==0:
		#while NUMTOCONV2 != 1:
			#if NUMTOCONV2 % 3 == 0:
				##note_digit(0)
				#digbat2=("0" + digbat2)
			#elif NUMTOCONV2 % 3 == 1:
				##note_digit(1)
				#digbat2=("+" + digbat2)
			#elif NUMTOCONV2 % 3 == 2:
				##note_digit(-1)
				#digbat2=("-" + digbat2)
			#NUMTOCONV2 = (NUMTOCONV2 + 1) // 3
		CRAD=-1
		CRADP=1
		digbat2=""
		for FNUM in str(NUMTOCONV2):
			BUFFD=(10**CRAD)
			BUFFC=(int(FNUM))
			while BUFFC > CRADP:
				BUFFC=(BUFFC*BUFFD)
				print BUFFC
				print "fo"
			CRAD -=1
			CRADP +=1
		print digbat2
		digbat3=(digbat + "." + digbat2)
	else:
		digbat3=digbat
	#print NUMTOCONV1
	#zero exception
	if (str(digbat3)==""):
		digbat="0"
	return(digbat3)
	
def btmul(numA, numB):
	numAcon=BTTODEC(numA)
	numBcon=BTTODEC(numB)
	decRes=(numAcon * numBcon)
	btRes=(DECTOBT(decRes))
	return(btRes)

def btadd(numA, numB):
	numAcon=BTTODEC(numA)
	numBcon=BTTODEC(numB)
	decRes=(numAcon + numBcon)
	btRes=(DECTOBT(decRes))
	return(btRes)

def btsub(numA, numB):
	numAcon=BTTODEC(numA)
	numBcon=BTTODEC(numB)
	decRes=(numAcon - numBcon)
	btRes=(DECTOBT(decRes))
	return(btRes)

#this should be a tad more acurate than its libbaltcalc counterpart. 
def btdev(numA, numB):
	numAcon=BTTODEC(numA)
	numBcon=BTTODEC(numB)
	decRes=(float(numAcon) / float(numBcon))
	print(decRes)
	btRes=(DECTOBT(decRes))
	return(btRes)


print(btdev("+", "+-"))
#print(BTTODEC(DECTOBT(55.3)))
print(DECTOBT(0.5))
#BTTODEC("+-0+.-")
print(BTTODEC("0.+-"))
#print(DECTOBT("1"))
#print uprad("+-0+.-0")
#print downrad("+-0+.-0")


