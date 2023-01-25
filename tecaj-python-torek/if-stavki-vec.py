#primerjava stevil

#kamn skarje papir

"""
program prejme 2 števili. --> input!!
če je njuna vsota večja od 500 ju sešteje
če je vsota majnša od 500 ju zmnoži
pol izpiše rezultat

789 567
49 72
249 251
"""

st1 = int(input())
st2 = int(input())

vsota = st1 + st2

if(vsota > 500):
	print(vsota)
elif(vsota < 500):
	print(st1 * st2)
else:
	print("Dej dve stevili k ne greta skupi v 500 prosim")


#Kamen škarje papir
#najprej prvi igralec pove potezo (kamen, papir ali škarje)
#potem drugi igralec pove potezo (kamen papir ali škarje)
#Ko oba igralca poveta potezo Povej kateri od njiju je zmagal.
#Če se je kateri zatipkal pri pisanju poteze to tudi sporoči

print("Kamen, Škarje, Papir! Vpiši najprej eno potezo, nato drugo potezo (kamen, skarje ali papir, vse z malo)")
poteza_prvi = input()
poteza_drugi = input()

if(poteza_prvi == "kamen" and poteza_drugi == "kamen"):
	print("Izenačeno!")
elif(poteza_prvi == "kamen" and poteza_drugi == "skarje"):
	print("Prvi zmaga!")
elif(poteza_prvi == "kamen" and poteza_drugi == "papir"):
	print("Drugi zmaga!")
elif(poteza_prvi == "skarje" and poteza_drugi == "kamen"):
	print("Drugi zmaga!")
elif(poteza_prvi == "skarje" and poteza_drugi == "skarje"):
	print("Izenačeno!")
elif(poteza_prvi == "skarje" and poteza_drugi == "papir"):
	print("Prvi zmaga!")
elif(poteza_prvi == "papir" and poteza_drugi == "kamen"):
	print("Prvi zmaga!")
elif(poteza_prvi == "papir" and poteza_drugi == "skarje"):
	print("Drugi zmaga!")
elif(poteza_prvi == "papir" and poteza_drugi == "papir"):
	print("Izenačeno!")
else:
	print("Hej, nekje si se zatipkal :(")

#gnezdenje if in prestopno leto + zodiak

if(poteza_prvi == "kamen"):
	if(poteza_drugi == "kamen"):
		print("Izenačeno")
	elif(poteza_drugi == "skarje"):
		print("Zmaga prvi")
	elif(poteza_drugi == "papir"):
		print("Zmaga drugi")
	else:
		print("Zatipkal si se pri drugem")
elif(poteza_prvi == "skarje"):
	if(poteza_drugi == "kamen"):
		print("Zmaga drugi")
	elif(poteza_drugi == "skarje"):
		print("Izenačeno")
	elif(poteza_drugi == "papir"):
		print("Zmaga prvi")
	else:
		print("Zatipkal si se pri drugem")
elif(poteza_prvi == "papir"):
	if(poteza_drugi == "kamen"):
		print("Zmaga prvi")
	elif(poteza_drugi == "skarje"):
		print("Zmaga drugi")
	elif(poteza_drugi == "papir"):
		print("Izenačeno")
	else:
		print("Zatipkal si se pri drugem")
else:
	print("Zatipkal si se pri prvem")

#Tretji nacin; kratko ampak malo manj pregledno

poteze = ["kamen", "skarje", "papir"]

if(poteza_prvi == poteza_drugi and poteza_prvi in poteze):
	print("Izenačeno")
elif((poteza_prvi == "kamen" and poteza_drugi == "skarje") or (poteza_prvi == "skarje" and poteza_drugi == "papir") or (poteza_prvi == "papir" and poteza_drugi == "kamen")):
	print("Zmaga prvi")
elif((poteza_prvi == "kamen" and poteza_drugi == "papir") or (poteza_prvi == "skarje" and poteza_drugi == "kamen") or (poteza_prvi == "papir" and poteza_drugi == "skarje")):
	print("Zmaga drugi")
else:
	print("Zatipkal si se")