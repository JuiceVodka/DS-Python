mojfajl = open("fajl.txt", "r")

#mojfajl.read()
#mojfajl.readline()
vrstice = mojfajl.readlines()
print(vrstice)

#trenutnaVrstica = None
#while(trenutnaVrstica != ""):
#	trenutnaVrstica = mojfajl.readline()
#	print(trenutnaVrstica)

vrstica = vrstica[:-1] # tako odstranimo zaden znak iz besede



mojfajl.close()


#with open("fajl.txt", "r") as mojfajl:
	#neka koda

#nadaljevanje -> automaticno close