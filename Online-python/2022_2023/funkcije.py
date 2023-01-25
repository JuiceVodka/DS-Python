print()
rezultat = input()
rezultat2 = int("5")
tip = type(5)
print(type(5))
print(type(int(input())))
beseda = str(578391)
range(10) #-> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(4, 7) #-> 4, 5, 6
range(2, 20, 3) #-> 2, 5, 8, 11, 14, 17


def nasaFunkcija(stevilo):
	for i in range(stevilo):
		print("to je funkcija")
	print()
	return(10)

rez = nasaFunkcija(5)
print(rez)

#Naloga:
#ploscine funkcija
#napisi funkcije, ki racunajo pliscine za naslednje like:
#kvadrat
#pravokotnik
#trikotnik
#kocka
#kvader
#vsaka funkcija sprejme tocno toliko podatkov kolikor jih rabi za izracun

def kvadrat(a):
	p = a*a
	return(p)

def pravokotnik(a, b):
	p = a*b
	return(p)

def trikotnik(a, va):
	return(a*va/2)

def kocka(a):
	return(6*a*a)

def kvader(a, b, c):
	return(2*a*b + 2*a*c + 2*b*c)

rez = kvadrat(17)
print(rez)

rez = pravokotnik(15, 3)
print(rez)

print(trikotnik(5, 3.2))

print(kocka(13))

print(kvader(12, 0.5, 101))

#naloga:
#iz vhoda (input()) preberi dve stevili
#napisi funkcijo, ki sprejme dve stevili in vrne njunega najvecjega skupnega delitelja
#to funkcijo pozeni z stevili iz inputa in izpisi rezultat

def gcd(st1, st2): #greatest common denominator -> ang. za najvecji skupni delitelj
	delitelj = 1
	if(st1 >= st2):
		for i in range(1, st2+1):
			if((st1%i == 0) and (st2%i == 0)):
				delitelj = i
	else:
		for i in range(1, st1+1):
			if((st1%i == 0) and (st2%i == 0)):
				delitelj = i
	return(delitelj)

#se najmanjsi skupni veckratnik
def nsv(st1, st2):
	veckratnik = 0
	if(st1 > st2):
		veckratnik = st1
	else:
		veckratnik = st2
	while((veckratnik % st1 != 0) or (veckratnik % st2 != 0)):
		veckratnik += 1
	return veckratnik

def nsv_napredno(st1, st2):
	return((st1*st2) / gcd(st1, st2))


st1 = int(input())
st2 = int(input())

print(gcd(st1, st2))
print("--------------------------")
print(nsv_napredno(st1, st2))
print("--------------------------")
print(nsv(st1, st2))
print("--------------------------")