"""S pomočjo while zanke izpiši naslednja št::
1. 8, 11, 14, 17, 20, . . . , 83, 86, 89  
2. 100, 98, 96, . . . , 4, 2.
3. AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG """

#stevila od 10 do 0
stevec = 10
while(stevec >= 0):
	print(stevec)
	stevec -= 1 

#stevila od 0 do 10
stevec = 0
while(stevec < 10):
	print(stevec)
	stevec = stevec + 1



print("---------------------------------")

stevilo = 8
while(stevilo < 90):
	print(stevilo)
	stevilo += 3


print("------------------------------------")

stevilo = 100
while(stevilo >= 2):
	print(stevilo)
	stevilo -= 2


print("----------------------------------------")

#AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG

beseda = ""

stevec = 0
while(stevec < 33):
	if(stevec < 10):
		beseda += "A"
	elif(stevec < 17):
		beseda += "B"
	elif(stevec < 25):
		if(stevec % 2 == 1):
			beseda += "C"
		else:
			beseda += "D"
	elif(stevec < 26):
		beseda += "E"
	elif(stevec < 32):
		beseda += "F"
	else:
		beseda += "G"

	stevec += 1

print(beseda)

pravilno = "AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG"

if(beseda == pravilno):
	print("PRAVILNO!")

beseda2 = ""

stevec = 0
while(beseda2 != pravilno):
	beseda2 += pravilno[stevec]
	stevec += 1

print(beseda2)

