#Ene par funkcij
spremenljivka = ""

a = type(spremenljivka)
print(a)



b = input()
print(b)

#Najdi quote (citat) iz svojega najljubsega filma oziroma najljubsi quote,
# ter naredi program, kjer te program vprasa da mu das citat in potem ga izpise 10x

print("Povej mi en citat")
citat = input()
print((citat + "\n") * 10)

#Na internetu najdi eno kitico s 4 vrsticami neke pesmi
#napisi program, ki te vprasa za vsak verz posebej 
#(npr. povej prvi verz, povej 2. verz itd)
#na koncu izpisi vse verze skupaj(stiri verzi, ena spremenljivka!) npr print(kitica)

print("____________________________")
print("Napisi mi prvi verz pesmi")
kitica = input()
kitica += "\n"

print("Napisi mi drugi verz pesmi")
kitica += input()
kitica += "\n"

print("Napisi mi tretji verz pesmi")
kitica += input()
kitica += "\n"

print("Napisi mi cetrti verz pesmi")
kitica += input()
kitica += "\n"

print("\nTvoja kitica je: \n" + kitica)
