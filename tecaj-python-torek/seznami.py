seznam = [15, 82, False, "beseda", 2, [1, 2, 3], "pet"]

seznam2 = [562, 5537198,"nova stvar", 6]

print(seznam2)
#dve funkciji; append() in remove()
seznam2.append(7)

print(seznam2)

seznam2.remove(5537198)

print(seznam2)

seznam2.append(6)
seznam2.append(6)
seznam2.append(6)
seznam2.append(6)
print(seznam2)

seznam2.remove(6)
print(seznam2)

nasElement = seznam[5]
print(nasElement)


dolzina = len(seznam)
print(dolzina)

zadnjiElement = seznam[len(seznam)-1]
print(zadnjiElement)


#naloga:
#Imaš dva seznama:
#seznam_prvi = [10, 20, 30, 40, 10]
#seznam_drugi = [10, 20, 30, 40, 50]
#preveri ali sta prva elementa seznamov enaka (True ce enaka ali False ce napacna) -> izpisi
#preveri ali sta zadnja elementa seznamov enaka (True ce enaka ali False ce napacna) -> izpisi

seznam_prvi = [10, 20, 30, 40, 10]
seznam_drugi = [10, 20, 30, 40, 50]

prvi_prvi = seznam_prvi[0]
drugi_prvi = seznam_drugi[0]

print(prvi_prvi == drugi_prvi)

prvi_zadnji = seznam_prvi[len(seznam_prvi) -1]
drugi_zadnji = seznam_drugi[len(seznam_drugi) -1]

print(prvi_zadnji == drugi_zadnji)

#seznam najljubsih stvari (sproti izgradimo)
#kaj si po horoskopu
#kaj si po kitajskem horoskopu

#if stavki