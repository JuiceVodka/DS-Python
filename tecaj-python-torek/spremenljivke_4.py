#pretvori iz kilogramov v funte in izpiši, 
#pri tem, da je 1 kg = 2,2 lb
#teže v kg (pretvori v lb): 60, 140, 20, 37, 112.5
#teže v lb (pretvori v kg): 135, 70, 225, 140, 600
#uporabljamo spremenljivke!
#ctrl shift d trenutno vrstico podvoji dol
pretvornik = 2.2
print(60 * pretvornik)
print(140 * pretvornik)
print(20 * pretvornik)
print(pretvornik * 37)
print(pretvornik * 112.5)

print(135 / pretvornik)
print(70 / pretvornik)
print(225 / pretvornik)
print(140 / pretvornik)
print(600 / pretvornik)


#preveri in izpisi logicno vrednost trditev
# 15 > 3
# 12 == 16
# 37.5 > 37.50
# 1069 <= 10000
# 1 != -1
# 1 < -1
# 472981 <= 903
logika = 15 > 3
print(logika)
logika = 12 == 16
print(logika)
logika = 37.5 > 37.50
print(logika)
logika = 1069 <= 10000
print(logika)
logika = 1 != -1
print(logika)
logika = 1 < -1
print(logika)
logika = 472981 <= 903
print(logika)

# Računanje z logičnimi vrednostmi
# Mi lahko več logičnih vrednosti združimo v eno
# tri operacije: and, or, not

a = True and False # rezultat take enačbe bo vedno ali True ali pa False

#and bo imel za rezultat True, samo takrat, ko je in desna stran in leva stran enaka True

b = 3 < 3 and 3 <= 3

#or

c = True or False

# or bo ime rezultat True, če je vsaj ena izmed strani (leva desna) enaka True

d = False
f = False
g = True

rezultat = g or (d and f) # tole bo True

#not -> negacija -> obrne logično vrednost tega na desni

neg = not True # tole bo False
neg2 = not False # tole bo True

neg3 = not (False and False) # tole bo True


"""
and:
	 A/B|true|false
		|----------|
	true|	T |	 F |
		|----------|
	false|	F |	 F |
		-----------

or:
	 A/B|true|false
		|----------|
	true|	T |	 T |
		|----------|
	false|	T |	 F |
		-----------

not:
	 A/B|true|false
		|----------|
		|	F |	 T |
		|----------|
	
"""

