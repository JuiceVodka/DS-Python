#napiši v spremeljivko svojo starost in jo izpiši v konzolo
startost = 22
print(startost)

#pretvorba kilometri milje
#naslednje količine pretvori med kilometri in miljami z uporabo spremelnivk in matematike
#pomagaj si z internetom!!
#km -> mi : 30, 12, 7, 1.8, 100, 67
#mi -> km : 0.6, 5, 30, 60, 8, 120, 363853

kilometriVmilje = 0.62137119224 # mik mi je 1 km
miljeVkilometri = 1.609344 #kok km je 1 mi

print(30 * kilometriVmilje)
print(12 * kilometriVmilje)
print(7 * kilometriVmilje)
print(1.8 * kilometriVmilje)
print(100 * kilometriVmilje)
print(67 * kilometriVmilje)

#drug nacin
print(30 / miljeVkilometri)
print(12 / miljeVkilometri)
print(7 / miljeVkilometri)
print(1.8 / miljeVkilometri)
print(100 / miljeVkilometri)
print(67 / miljeVkilometri)

print(0.6 * miljeVkilometri)
print(5 * miljeVkilometri)
print(30 * miljeVkilometri)
print(60 * miljeVkilometri)
print(8 * miljeVkilometri)
print(120 * miljeVkilometri)
print(363853 * miljeVkilometri)


#Pretvori stopinje v radiane uporabi internet!!!
#deg = stopinje
#rad = radiani
#deg -> rad : 1, 30, 60, 90, 180, 270, 235, 17
#rad -> deg : 3.14, 1, 6.28, 10, 5, 15

const = 3.14 / 180

print(1 * const)
print(30 * const)
print(60 * const)
print(90 * const)
print(180 * const)
print(270 * const)
print(235 * const)
print(17 * const)

print("")

print((3.14 / const) %360)
print((1 / const) %360)
print((6.28 / const) %360)
print((10 / const) %360)
print((5 / const) %360)
print((15 / const) %360)

#naredi 5 spremenljivk in jih daj v enačbo. Uporabit moraš vsaj 3 različne matematične operacije 
#in rezultat enačbe mora biti 333

prva = 1
druga = 333
tretja = 20
cetrta = 10
peta = 2

print((druga / prva) + tretja - (cetrta * peta))


print("------------------------------------------")
#Logične vrednosti oziroma boolean
#True
#False

logika = True
print(logika)

logikaDva = False
print(logikaDva)

primerjava = 15 > 3
print(primerjava)

15 > 3
15 < 3
15 >= 3
15 <= 3
15 == 3 #Dva enacaja !!!!
15 != 3

#preveri in izpisi logicno vrednost trditev

