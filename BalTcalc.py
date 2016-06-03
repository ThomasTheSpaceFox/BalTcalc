#!/usr/bin/env python
HELPTEXT=('''---help---
useable balanced ternary notation conventions:
+,1 (positive)
0,0 (zero/ground state)
-.T (negative)

-command(/altcommand(s))--:--description-
bt-dec/btdec/bttodec: convert a balanced ternary number to decimal
invert/btinvert     : invert a balanced ternary number. 
   i.e. -+0+ would become +-0-
help/?              : this help
quit                : quit BalTcalc
''')
ABOUTTEXT=('''---about---
BalTcalc v0.1
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
	if (USRENTRY==("invert") or USRENTRY==("btinvert")):
		print("number to invert?")
		numtoinv = libbaltcalc.BTstrgetsort()
		print(libbaltcalc.BTINVERT(numtoinv))
	if (USRENTRY==("help") or USRENTRY==("?")):
		print(HELPTEXT)
	if (USRENTRY==("about") or USRENTRY==("version")):
		print(ABOUTTEXT)
