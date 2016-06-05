#!/usr/bin/env python
HELPTEXT=('''---help---
useable balanced ternary notation conventions:
+,1 (positive)
0,0 (zero/ground state)
-.T (negative)

-command(/altcommand(s))--:--description-
bt-dec/btdec/bttodec: convert a balanced ternary number to decimal
dec-bt/decbt/dectobt: convert a decimal number to balanced ternary
invert/btinvert     : invert a balanced ternary number. 
   i.e. -+0+ would become +-0-
add/btadd           : preform addition in balanced ternary
mul/btmul           : preform multiplication in balanced ternary
sub/btsub           : preform subtraction in balanced ternary
dev/btdev           : preform division in balanced ternary
help/?              : this help
quit                : quit BalTcalc
''')
ABOUTTEXT=('''---about---
BalTcalc v0.2
(c)2016 Thomas Leathers

  BalTcalc is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
  
  BalTcalc is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with BalTcalc. If not, see <http://www.gnu.org/licenses/>
''')
import libbaltcalc
print ("BalTcalc v0.1 ready")
USRENTRY="null"
while USRENTRY!=("quit"):
	USRENTRY = raw_input(':')
	if (USRENTRY==("bt-dec") or USRENTRY==("btdec") or USRENTRY==("bttodec")):
		print("number to convert?")
		numtocon = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.BTTODEC(numtocon))
	if (USRENTRY==("dec-bt") or USRENTRY==("decbt") or USRENTRY==("dectobt")):
		print("number to convert?")
		numtocon = raw_input('>:')
		numtocon=int(numtocon)
		print(libbaltcalc.DECTOBT(numtocon))
	if (USRENTRY==("invert") or USRENTRY==("btinvert")):
		print("number to invert?")
		numtoinv = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.BTINVERT(numtoinv))
	if (USRENTRY==("help") or USRENTRY==("?")):
		print(HELPTEXT)
	if (USRENTRY==("about") or USRENTRY==("version")):
		print(ABOUTTEXT)
	if (USRENTRY==("add") or USRENTRY==("btadd")):
		print("first number?")
		numtoaddA = libbaltcalc.BTstrgetsort()
		print("second number?")
		numtoaddB = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.btadd(numtoaddA, numtoaddB))
	if (USRENTRY==("mul") or USRENTRY==("btmul")):
		print("first number?")
		numtoaddA = libbaltcalc.BTstrgetsort()
		print("second number?")
		numtoaddB = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.btmul(numtoaddA, numtoaddB))
	if (USRENTRY==("sub") or USRENTRY==("btsub")):
		print("first number?")
		numtoaddA = libbaltcalc.BTstrgetsort()
		print("second number?")
		numtoaddB = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.btsub(numtoaddA, numtoaddB))
	if (USRENTRY==("dev") or USRENTRY==("btdev")):
		print("first number?")
		numtoaddA = libbaltcalc.BTstrgetsort()
		print("second number?")
		numtoaddB = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.btdev(numtoaddA, numtoaddB))
		
		
