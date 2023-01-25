#Ctrl + c -> ustavi neskončno zanko tako da ustavi cel program

"""
while True: #to je neskončna zanka
	print("zanka")

print("Zunaj zanke")
"""
"""
števec = 0

while(števec < 10): #10x izpis zanka
	print("zanka")
	števec += 1
"""

#napiši zanko, ki se izvaja v neskončnost, in vsakič izpiše kolikokrat se je že izvedla
"""stevec = 0
while(True):
	print(stevec)
	stevec += 1
"""

#Uporabnik vnese število. Naredi zanko ki se izvede tolikokrat kot je uporabnik vnesel
#in vsakič izpiše kolikokrat se je izvedla
stevilo = int(input())
stevec = 1

while(stevec <= stevilo):
	print(stevec)
	stevec += 1


#napiši zanko, ki se izvede 10x in vsakič tolikrat v isti vrstici izpiše "Zanka" 
#kolikokrat se je izvedla

stevec = 1
while(stevec <= 10):
	print("Zanka" * stevec)
	stevec += 1

#Napiši zanko, ki izpiše vsa števila od 10 do 0

stevilo = 10
while(stevilo >= 0):
	print(stevilo)
	stevilo -= 1

#Izpiši vsa soda števila med 0 in 100

sodo = 0
while(sodo < 102):
	print(sodo)
	sodo += 2


#liha stevila
liho = 1
while(liho < 102):
	print(liho)
	liho += 2


#tudi resitev ampak reje naredi kot zgoraj
stevec = 0
while(stevec <= 100):
	if(stevec % 2 == 0):
		print(stevec)
	stevec += 1