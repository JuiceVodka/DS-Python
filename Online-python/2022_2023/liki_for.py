#s for zanko v konzolo narisi trikotnik (pravokotni)
#visino dobis od uporabnika z input()
visina = int(input())
"""
* 1.
* * 2.
* * * 3.
* * * * 4.
"""
for i in range(visina):
	izpis = ""
	#Sestavi izpis
	for j in range(i+1):
		izpis += "* "
	print(izpis)

for i in range(visina):
	print("* " * (i+1))
#izpisi ta trikotnik se tako, da je zrcaljen cez navpico crto (gleda v drugo stran)
"""
      * 
    * * 
  * * * 
* * * * 
"""
for i in range(visina):
	izpis = ""
	#dodaj presledke
	for h in range(visina - i):
		izpis += "  "

	#Sestavi izpis
	for j in range(i+1):
		izpis += "* "
	print(izpis)

for i in range(visina):
	print(" " * ((visina - i) * 2) + "* " * (i+1))

#izpisi enakostni trikotnik
"""
   * 
  * * 
 * * * 
* * * * 
"""
for i in range(visina):
	izpis = ""
	#dodaj presledke
	for h in range(visina - i):
		izpis += " "

	#Sestavi izpis
	for j in range(i+1):
		izpis += "* "
	print(izpis)

for i in range(visina):
	print(" " * (visina - i) + "* " * (i+1))
#izpisi kvadrat
"""
* * * * 
* * * * 
* * * * 
* * * * 
"""
for i in range(visina):
	izpis = ""
	for i in range(visina):
		izpis += "* "
	print(izpis)

print()

for i in range(visina):
	print(visina * "* ")

print()

#izpisi bozicno smrekco, ki ima toliko delov, kolikor damo visino

for delSmreke in range(1, visina+1):
	for i in range(delSmreke):
		print(" " * ((visina - delSmreke) + (delSmreke - i)) + "* " * (i+1))


print()

for delSmreke in range(1, visina+1):
	for i in range(delSmreke):
		izpis = ""

		#dodaj presledke za vsak del smreke (vsak cel trikotnik)
		for zacetni in range(visina - delSmreke):
			izpis += " "

		#dodaj presledke
		for h in range(delSmreke - i):
			izpis += " "

		#Sestavi izpis
		for j in range(i+1):
			izpis += "* "
		print(izpis)

#ploscine funkcija
#navecji skupni deljjitelj
#kamen skarje papir