import time
seznam = [12, 15, 32, 42, 55, 75, 150, 122, 132, 180, 200]

for i in seznam:
	print(i)
	break

#Izpiši vsa praštevila med 1 in 50
#Deljivost preverimo tako, da pogledamo, ce je ostanek prideljenju z nekim stevilom enak 0
#ostanek pri deljenji ==> a%b --> ostanek pri deljenju a z b
start = time.time()
for stevilo in range(1, 1000):
	prastevilo = True
	for delitelj in range(2, int(stevilo/2)):
		if(stevilo%delitelj == 0):
			print(str(stevilo) + " ni prastevilo!")
			prastevilo = False
			break
	if(prastevilo):
		print(str(stevilo) + " je prastevilo")
end = time.time()
print(end-start)

#seznam = [12, 15, 32, 42, 55, 75, 150, 122, 132, 180, 200]
#pojdi cez vse elemente seznama in napisi (s for zanko)
#ce je stevilo manjse od 15 izpisi :Manjse od 15
#ce je vecje ali enako od 15 in manjse od 50 izpisi med 15 in 50
#ce je vecje ali enako od 50 in mansje od 75 izpisi med 50 in 75
#ce je vecje ali enako od 75 izpisi vec od 75

seznam = [12, 15, 32, 42, 55, 75, 150, 122, 132, 180, 200]

for i in seznam:
	if(i < 15):
		print("Manjse od 15")
	elif(i >= 15 and i < 50):
		print("Med 15 in 50")
	elif(i >= 50 and i < 75):
		print("Med 50 in 75")
	elif(i >= 75):
		print("Vecje od 75")
