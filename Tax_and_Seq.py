#!/usr/bin/python
import re
import sys
print 'sys.argv is', sys.argv

script = sys.argv[0]
staryPlik = sys.argv[1]
nowyPlikTX = str("TX_" + staryPlik)
nowyPlikSE = str("SE_" + staryPlik)

new_fileTX = open("./" + nowyPlikTX, 'w')  
new_fileSE = open("./" + nowyPlikSE, 'w')

RODZEU=["Colacium", "Cryptoglena", "Euglena", "Euglenaria", "Euglenaformis", "Monomorphina", "Trachelomonas", "Strombomonas"]
RODZPH=["Discoplastis", "Lepocinclis", "Phacus", "Phacus1", "Phacus2", "Discoplastis2", "Discoplastis1", "Flexiglena"]
RODZEUT=["Eutr"]
Rodzaje=["Colacium", "Cryptoglena", "Discoplastis", "Discoplastis2", "Discoplastis1", "Euglena", "Euglenaria", "Eutr", "Euglenaformis", "Monomorphina", "Lepocinclis", "Phacus", "Phacus1", "Phacus2", "Trachelomonas", "Strombomonas", "Flexiglena"]				

for line in open(staryPlik, 'r'):
	line = line.rstrip()
	if line.find(">"): # czyli jezeli nie ma >
		new_fileSE.write(line + "\n")

	else: # jezeli jest = nazwy seq
		taxline = line
		for rodzEu in RODZEU:
			taxline = taxline.replace("|"+ rodzEu + "_" , "\tD_0__Eukaryota;D_1__Excavata;D_2__Discoba;D_3__Euglenida;D_8__Euglenaceae;D_9__" + rodzEu + ";D_10__" + rodzEu + " ")
		for rodzPh in RODZPH:
			taxline = taxline.replace("|"+ rodzPh + "_" , "\tD_0__Eukaryota;D_1__Excavata;D_2__Discoba;D_3__Euglenida;D_8__Phacaceae;D_9__" + rodzPh + ";D_10__" + rodzPh + " ")
		for rodzEut in RODZEUT:
			taxline = taxline.replace("|"+ rodzEut + "_" , "\tD_0__Eukaryota;D_1__Excavata;D_2__Discoba;D_3__Euglenida;D_8__Eutreptiales;D_9__" + rodzEut + ";D_10__" + rodzEut + " ")

		taxline = taxline.replace("|" , "_")
		taxline = taxline.replace(">" , "")
		
		fasline = line.replace("|", "_")
		
		for rodz in Rodzaje:
			fasline = re.sub("_" + rodz + "_\w*" , "", fasline)
		
		new_fileTX.write(taxline + "\n")
		new_fileSE.write(fasline + "\n")

new_fileSE.close()
new_fileTX.close()
