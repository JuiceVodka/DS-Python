#s pomocjo while zanke sestej vsa stevila od 1 do 20 in izpisi rezultat
#1 + 2 + 3 + 4 + 5 + 6 + 7 +.....+20

stevec = 1
vsota = 0
while(stevec <= 20):
	vsota += stevec
	stevec += 1

print(vsota)
print("------------------------------------")

#s pomocjo while zanke izpiši zmnozek trenutne vrednost stevca (od 1 do 20) in prejsnje vrednosti
#0*1, 1*2, 2*3, 3*4, 4*5, ...., 19*20
#hint: uporabi dve spremenljivki, ena naj bo stevec, druga pa naj hrani prejsno vrednost

trenutna = 1
prejsna = 0

while(trenutna <= 20):
	print(trenutna * prejsna)
	prejsna = trenutna
	trenutna += 1

stevec = 1
while(stevec <= 20):
	print(stevec * stevec - 1)
	stevec += 1


#s pomocjo while zanke izracunaj vrednost naslednjega zaporedja:
#1 - 2 + 3 - 4 + 5 - 6 +...... + 1999 - 2000

print("--------------------------------------")
stevec = 1
vsota = 0

while(stevec <= 2000):
	if(stevec % 2 == 1): #0 --> False; vse ostalo ---> True
		vsota += stevec
	else:
		vsota -= stevec
	stevec += 1
print(vsota)

print("----------------------------------------")

#Glavna naloga: Fibonaccijevo zaporedje
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 34+21 == 55, 34 + 55 == 89 ....
#Naloga: s pomocjo while zanke izpisi prvih 20 stevil fibonaccijevega zaporedja.
# Uporabi tri spremenljivke

rezultat = 0
prejsnje = 1
predprejsnje = 0
print(predprejsnje)
print(prejsnje)
i = 0
while(i in range(20)):
	rezultat = prejsnje + predprejsnje
	predprejsnje = prejsnje
	prejsnje = rezultat
	print(rezultat)
	i += 1


# Izpisi 100-to stevilo v fibonaccijevem zaporedju
rezultat = 0
prejsnje = 1
predprejsnje = 0
print(predprejsnje)
print(prejsnje)
i = 0
while(i in range(100)):
	rezultat = prejsnje + predprejsnje
	predprejsnje = prejsnje
	prejsnje = rezultat
	i += 1
print(rezultat)

# Izpisi te obe nalogici z uporabo for zanke


rezultat = 0
prejsnje = 1
predprejsnje = 0
print(predprejsnje)
print(prejsnje)
i = 0
for i in range(20):
	rezultat = prejsnje + predprejsnje
	predprejsnje = prejsnje
	prejsnje = rezultat
	print(rezultat)
	i += 1

#--------------------------

rezultat = 0
prejsnje = 1
predprejsnje = 0
for i in range(100):
	rezultat = prejsnje + predprejsnje
	predprejsnje = prejsnje
	prejsnje = rezultat
print(rezultat)