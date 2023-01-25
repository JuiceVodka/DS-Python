
"""
x + 1 = 7 
x = ?

x + y = 7
y = 3

x = ?

-----------------------"""

mojaSpremenljivka = 7

print(mojaSpremenljivka + 3)


mojaSpremenljivka = 6

print(mojaSpremenljivka + 3)


drugaSpremeljivka = 2

test = 15

print(drugaSpremeljivka + test)


sestavljena = drugaSpremeljivka + test

print(sestavljena)

drugaSpremeljivka = 3

print(sestavljena)


#Naloga: napiši python program, kjer imaš eno spremenljivko za vsak mesec v letu
#vsaka ma vrednost tok kolikor je dnevov v tistem mesecu

januar = 31
februar = 28
marec = 31
april = 30
maj = 31
junij = 30
julij = 31
august = 31
september = 30
oktober = 31
november = 30
december = 31

#Izpiši koliko dni ima februar
print(februar)
#Izpiši koliko dni imajo skupaj junij julij august
print(junij + julij + august)
#izpiši koliko dni imata skupaj februar in december
print(februar + december)
#izpiši koliko dni imajo skupaj vsi meseci od januarja do julija
print(januar + februar + marec + april + maj + junij + julij)
#izpiši koliko dni imajo skupaj vsi meseci brez septembra
print(januar + februar + marec + april + maj + junij + julij + august + september + oktober + november + december - september)

#----------------------

print(januar - februar)
print(januar * februar)
print(januar / februar)
print(februar - januar)

#vse naslendje naloge delamo tako, da rezultat shranimo v eno spremenljivko
#ki jo potem spreminjamo in na vsakem koraku izpisujemo --> jota
#lahko si naredite kolikor hocete pomoznh spremenljivk
print("-------------------------------------------------")
#koliko dni ima februar manj kot avgust
jota = august - februar
print(jota)

#koliko ur je v teh dneh
ure = 24
jota = ure * jota
print(jota)

#koliko ur je v celem letu
dni = januar + februar + marec + april + maj + junij + julij + august + september + oktober + november + december
jota = dni * ure
print(jota)

#koliko ur je v prestopnem letu
jota = (dni + 1) * ure
print(jota)

#koliko ur je v prestopnem letu brez februarja
jota = (dni - februar) * ure
print(jota)

#koliko ur je v navadnem letu brez februarja
jota = (dni - februar) * ure
print(jota)

#koliko polnih tednov je v januarju
teden = 7
jota = januar / teden
print(jota)

"""
% -> ostanek pri deljenju

8%7 -> 1
10%4 -> 2
31%7 -> 3
"""

jota = (januar - januar%teden) / teden
print(jota)
