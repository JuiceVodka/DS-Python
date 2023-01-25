vrednost = [5, "b", [10, 2, True]]
jeVSeznamu = 5 in vrednost
vrednost.append("nova stvar v seznamu")
vrednost[2].remove(10)
drugiElement = vrednost[-1]

if(10 in vrednost[2]):
	print("a")
elif(True in vrednost[2]):
	print("elif")
else:
	print("b")
print("c")

print()
rezultat = input()
int()
str()
type()

mojFajl = open("fajl.txt", "r")

#mojFajl.read()
#mojFajl.readline()
mojFajl.readlines()

mojFajl.close()

while(mojFajl.readLine() != ""):
	print("ponavljanje")

print(konec)


while(True):
	print("neskončnost")
	break
	print("neskončnost 2")

print("nadaljevanje")


stevec = 0
while(stevec < 10):
	stevec += 1
	print(stevec)