seznam = [1, 2, 3, 5, 7]

for poljubno_ime in seznam:
	print(poljubno_ime)

#s for znako izpis vseh števil od 0 do 22

for stevilo in range(23):
	print(stevilo)

#for zanka izpis stevil od 5 do 17

for stevilo in range(5, 18):
	print(stevilo)


#for zanka, stevila od 2 do 106, vsako stevilo je za 4 vecje od prejsnega

for stevilo in range(2, 107, 4):#inkrement
	print(stevilo)


#s pomocjo for zanke izpisi vsa soda stevila med 0 in 100
for i in range(0, 101, 2):
	print(i)


#s pomocjo for zanke izpisi vsa liha stevila med 0 in 100
for i in range(1, 100, 2):
	print(i)


#s pomocjo for zanke izpisi vsa soda stevila med 100 in 0
for i in range(100, -1, -2):
	print(i)


#s pomocjo for zanke izpisi vsa liha stevila med 100 in 0
for i in range(99, 0, -2):
	print(i)


#Risanje likov

#primer:
#iz vhoda preberi stevilo in izrisi vodoravno crto dolgo toliko kot je stevilo
stevilo = int(input("Vnesi dolzino crte:  "))

#1
print("* " * stevilo)

#2
besedaZaizpis = ""
for i in range(stevilo):
	besedaZaizpis += "* "
print(besedaZaizpis)


#iz vhoda preberi stevilko in izpisi navpicno crto visoko toliko kot je stevilo
stevilo = int(input("Vnesi visino crte:  "))

for i in range(stevilo):
	print("* ")
