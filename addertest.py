#!/usr/bin/env python
#test script for libbaltcalc's addition function.
import libbaltcalc
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
