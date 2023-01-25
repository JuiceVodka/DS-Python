seznam = [1, "s", "fhasjf", True, [1, 2, 3]]

tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


#indexiranje v seznamu!!
#iz prvega seznama hocem dobiti prvi in dugi element
seznamKrajši = [seznam[0], seznam[1]]
seznamKrajšiIndeksirano = seznam[0:2] #dvopičje pomeni od - do 
#-> element z inexom do je zgornja meja, v novi tabeli ga ne bo!!
print(seznamKrajšiIndeksirano)
print(seznam)

#iz prvega seznama mi daj vse elemente razen zadnjega
seznamVsiRazenZadnjega = seznam[0:len(seznam)-1]
print(seznamVsiRazenZadnjega)
seznamVsiRazenZadnjega = seznam[0:-1]
print(seznamVsiRazenZadnjega)

#iz prvega seznama daj elemente od drugega do cetrtega
seznamDrugiDoCetrti = seznam[1:4]
print(seznamDrugiDoCetrti)

#iz seznama daj vse elemente od prevega do zadnjega
seznamCel = seznam[0:len(seznam)]
print(seznamCel)

#s tem trikom lahko tudi na primer odstranimo crke iz besede
beseda = "Ne teci po hodniku!"
#besedi odstrani klicaj
beseda = beseda[0:-1]
print(beseda)

#ce imamo na levi strani dvopicja 0, ali pa na desni strani len(seznam)
#(torej zacetek na eni strani in konec seznama na drugi strani)
#lahko to izpiustimo

seznamBrezZadnjega = seznam[:-1]
print(seznamBrezZadnjega)

#od drugega do konca
seznamBrezPrvega = seznam[1:]
print(seznamBrezPrvega)

seznamCelElegantno = seznam[:]
print(seznamCelElegantno)


tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#dostop do elementov tabele
print(tabela)
prvaVrstica = tabela[0]
drugaVrstica = tabela[1]
tretjaVrstica = tabela[2]
print(prvaVrstica)
print(drugaVrstica)
print(tretjaVrstica)

drugiElementPrveVrstice = tabela[0][1]
print(drugiElementPrveVrstice)

zadnjiElementZadnjeVrstice = tabela[2][2]
print(zadnjiElementZadnjeVrstice)

drugiElementDrugeVrstice = tabela[1][1]
print(drugiElementDrugeVrstice)

drugiInTretjiElementPrveVrstice = tabela[0][1:]
print(drugiInTretjiElementPrveVrstice)


#križci krožci
#clovek ne jezi se