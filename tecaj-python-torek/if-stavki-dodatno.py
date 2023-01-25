#Uporabnik vnese stevilko in mi mu povemo ali to je prestopno leto
#Izpiši ali "#### je prestopno leto" ali "#### ni prestopno leto"


letnica = int(input())

if((letnica % 4 == 0 and letnica % 100 != 0) or letnica % 400 == 0):
	print(str(letnica) + " je prestopno leto")
else:
	print(str(letnica) + " ni prestopno leto")


if(letnica % 400 == 0):
	print(str(letnica) + " je prestopno leto")
elif(letnica % 100 == 0):
	print(str(letnica) + " ni prestopno leto")
elif(letnica % 4 == 0):
	print(str(letnica) + " je prestopno leto")
else:
	print(str(letnica) + " ni prestopno leto")


#Poln horoskop
#Uporabnika najprej vprašamo: "Katerega meseca si rojen (številka)"
#Preberemo številko z vhoda
#Potem ga vprašamo: "Katerega dneva v mesecu si rojen (številka)"
#preberemo številko z vhoda

#Nato uporabmniku izpišemo kaj je po horoskopu, z katerimi znamenji se najbolj ujame ter
#mesecno napoved

horoskopi = ["Zatipkal si se :(", "Kozorog", "Vodnar", "Ribi", "Oven", "Bik", "Dvojčka", "Rak", "Lev", "Devica", "Tehtnica", "Škorpijon", "Strelec"]

ujemanja = ["", "Z Bikom in z Devico, pa tudi z Rakom, z Ribama in s Škorpijonom", "Z Dvojčkoma in s Tehtnico, pa tudi z Levom, z Ovnom in s Strelcem", "S Škorpijonom in z Rakom, pa tudi z Devico, s Kozorogom in z Bikom", "Se (ponavadi) dobro ujema z Levom in s Strelcem, pa tudi s Tehtnico, z Dvojčkoma in z Vodnarjem", "Z Devico in s Kozorogom, pa tudi s Škorpijonom, z Ribo in z Rakom", "S Tehtnico in z Vodnarjem, pa s Strelcem, z Levom in z Ovnom", "S Škorpijonom in z Ribo, pa s Kozorogom, z Devico in z Bikom", "S Strelcem in z Ovnom, pa tudi s Tehtnico, z Vodnarjem in z Dvojčkoma", "S Kozorogom in z Bikom, pa tudi z Ribama, s Škorpijonom in z Rakom", "Z Dvojčkoma in z Vodnarjem, pa tudi z Ovnom, z Levom in s Strelcem", "Z Ribama in z Rakom, pa tudi z Bikom, z Devico in s Kozorogom", "Z Ovnom in z Levom, pa tudi z Dvojčkoma, s Tehtnico in z Vodnarjem"]

napoved = ["", "Napolnite telo z energijo, prav tako pa poskrbite tudi za veselje in dobro počutje. Danes se odločite za nov začetek. Pripravljeni boste na akcijo, ki pa je ne boste dočakali, če sami ne boste naredili nič za premik naprej. Doma bo mirno, zato se boste morda celo rahlo dolgočasili. Zdravje: odlično!", "Tudi danes boste pri delu zelo zagnani. Pričakujete lahko klice nadrejenih, ki vas bodo spodbujali k večji storilnosti, vi pa jim boste brez ugovarjanja le prikimali. Ker niste stroj, bodite pazljivi, da se ne bo vaše počutje obrnilo na slabše. Konflikti v službi bodo mimo, zato bo vzdušje prijetnejše. Pazite na zdravje!", "Pazite nase in na svoje telo, prav tako premislite o telesni dejavnosti. Loteva se vas prehlad, ki bi vas lahko za nekaj dni položil v posteljo. Na področju dela se bodo lahko prav danes pojavijo spori. Nesoglasja med delavci so vsakdanja stvar, zato poskušajte uveljaviti svojo vlogo popolnega diplomata. Finančne težave vam bodo še vedno kratile spanec. Previdno!", "Tudi današnji dan vam ne bo pisan na kožo. Problematika v odnosih bo še vedno v ospredju. Zdelo se vam bo, da vas prav nihče ne razume! Pričakujte težaven delavnik, saj so možni konflikti in nevšečnosti pri delu. Zvečer pa si le privoščite oddih. Mozaik želja za vas ta trenutek ni dosegljiv! Ne plujte proti toku!", "Zdelo se vam bo, da vam nekaj leži na duši, pa tega ne boste zmogli povedati najbližjim. Prav je, da razmislite, komu lahko dejansko zaupate. Pogovor in izpoved vam bosta dobro dela. Previdni pa bodite na zdravstvenem področju. Zdravje vas bo namreč prav danes lahko pustilo na cedilu! Poskrbite zase in se razvajajte!", "Današnji dan bo prav poseben, saj bo primeren za nova poznanstva in sklepanje novih prijateljstev. Bodite strpni in ne prehitevajte dogajanja. Čutili boste, kako s svojo energijo vplivate na ljudi okoli sebe. Previdno pri zdravju! Na delovnem mestu ne izgubljajte energije z nepomembnimi stvarmi. Pretehtajte, kaj je zares pomembno in kaj ni.", "Danes bo napočil trenutek, da vsem pokažete, kdo ste in koliko veljate. Stvari se bodo odvijale kar same od sebe; po vaših načrtih in pričakovanjih, brez da bi se vi za to morali kaj truditi. Finančno stanje je solidno, kmalu si boste lahko privoščili tudi krajše počitnice, po katerih toliko hrepenite. S tem si boste napolnili baterije in se pripravili na nov uspeh.", "Danes bo napočil trenutek, da vsem pokažete, kdo ste in koliko veljate. Stvari se bodo odvijale kar same od sebe; po vaših načrtih in pričakovanjih, brez da bi se vi za to morali kaj truditi. Finančno stanje je solidno, kmalu si boste lahko privoščili tudi krajše počitnice, po katerih toliko hrepenite. S tem si boste napolnili baterije in se pripravili na nov uspeh.", "Pri telesnih aktivnostih bodite danes še posebej pozorni, da ne bi prišlo do raznih poškodb ali ureznin. Pazite tudi pri vožnji, prilagodite hitrost na cesti in bodite še dodatno pozorni v naseljih in v bližini otrok. Avto prej preglejte, da se vam ne bo kaj na poti pokvarilo, saj bi si ustvarili samo dodatne stroške. Pazite tudi na hrano in pijačo.", "Sonce vas bo dokaj utrudilo, zato boste začeli razmišljati o tem, da bi preostanek dneva enostavno prespali. Utrujenost vas sicer daje že dalj časa in imate občutek, kot da se nikakor ne morete naspati. Izkoristite dan za to, da si boste povrnili malo moči. Naspite se in se tako spočijte.", "Že dopoldan boste občutili krizo. Še vedno se niste naučili, kako načrtovati odlive z bančnega računa. Skrajni čas je, da se naučite, saj se vam drugače ne piše dobro. Naslednjič načrtujte porabo sredstev vnaprej. Dan bo zelo naporen, saj ne čutite več strasti in zagnanosti, kot ste ju nekoč. Odkrijte recept za zadovoljstvo!", "Planeti tudi danes ne bodo naklonjeni prijateljskim in družinskim odnosom. Prepiri so vidni tako v partnerstvu kot pri delu. Osredotočite se na obveznosti. Razum bo na vaši strani, zato se boste kljub zapletom uspešno lotevali novih izzivov. Ne pozabite na načrtovanje porabe vaših sredstev. Sprejmite trenutne finančne omejitve, saj se vam drugače ne piše dobro!"]

mesec = int(input("Katerega meseca si rojen (številka):    "))

dan = int(input("Katerega dneva v mesecu si rojen (številka):	"))

horoskop = -1


if(mesec < 1 or mesec > 12):
	horoskop = 0
elif(mesec == 1):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 20):
		horoskop = 1
	else:
		horoskop = 2
elif(mesec == 2):
	if(dan < 1 or dan > 29):
		horoskop = 0
	elif(dan <= 18):
		horoskop = 2
	else:
		horoskop = 3
elif(mesec == 3):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 20):
		horoskop = 3
	else:
		horoskop = 4
elif(mesec == 4):
	if(dan < 1 or dan > 30):
		horoskop = 0
	elif(dan <= 19):
		horoskop = 4
	else:
		horoskop = 5
elif(mesec == 5):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 20):
		horoskop = 5
	else:
		horoskop = 6
elif(mesec == 6):
	if(dan < 1 or dan > 30):
		horoskop = 0
	elif(dan <= 20):
		horoskop = 6
	else:
		horoskop = 7
elif(mesec == 7):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 22):
		horoskop = 7
	else:
		horoskop = 8
elif(mesec == 8):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 22):
		horoskop = 8
	else:
		horoskop = 9
elif(mesec == 9):
	if(dan < 1 or dan > 30):
		horoskop = 0
	elif(dan <= 22):
		horoskop = 9
	else:
		horoskop = 10
elif(mesec == 10):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 23):
		horoskop = 10
	else:
		horoskop = 11
elif(mesec == 11):
	if(dan < 1 or dan > 30):
		horoskop = 0
	elif(dan <= 21):
		horoskop = 11
	else:
		horoskop = 12
elif(mesec == 12):
	if(dan < 1 or dan > 31):
		horoskop = 0
	elif(dan <= 21):
		horoskop = 12
	else:
		horoskop = 1

print("\nPo horoskopu si: " + horoskopi[horoskop] + "\n")
if(horoskop > 0):
	print("Najbolje se ujemaš " + ujemanja[horoskop] + "\n")

	print("Napoved:\n" + napoved[horoskop])
