
#naš program bo prejel število iz inputa od uporabnika
#in napisal "Število je pozitivno" če je števiko pozitivno
#ali "Število je negativno" če je število negativno

stevilo = int(input())

if(stevilo > 0):
	print("Število je pozitivno!")
#else:
#	print("Število je negativno")

if(stevilo < 0):
	print("Število je negativno")

print("Konec programa")


#Naloga: Uporabnik vnese oceno, ki jo dobil v šoli (od 1 do 5)
#glede na oceno, ki jo je dobil, mu napišite pohvalo, ali pa ga okregajte
#nadaljevanje; če upoprabnik vnese število, ki ni med 1 in 5 mu povejte da naj
#napiše pravo oceno

ocena = int(input())

if(ocena == 1):
	print("začni se učit >:(")
elif(ocena == 2):
	print("Potrebuješ še veliko vaje")
elif(ocena == 3):
	print("V redu je")
elif(ocena == 4):
	print("Bravo ! :D")
elif(ocena == 5):
	print("Dbest, wow, hcem biti tak kot ti <3")
else:
	print("Zakvaj mi lažeš :(")
