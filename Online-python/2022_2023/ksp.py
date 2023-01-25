import math
import random
import os
import time

#art = """                              Y\     /Y
#                              | \ _ / |
#        _____                 | =(_)= |
#    ,-~"     "~-.           ,-~\/^ ^\/~-.
#  ,^ ___     ___ ^.       ,^ ___     ___ ^.
# / .^   ^. .^   ^. \     / .^   ^. .^   ^. \
#Y  l    O! l    O!  Y   Y  lo    ! lo    !  Y
#l_ `.___.' `.___.' _[   l_ `.___.' `.___.' _[
#l^~"-------------"~^I   l^~"-------------"~^I
#!\,               ,/!   !                   !
# \ ~-.,_______,.-~ /     \                 /
#  ^.             .^       ^.             .^    -Row
#    "-.._____.,-"           "-.._____.,-"#
#
#               ->Mr&MrsPacman<-"""
"""
print(art)

os.system()

print(art)

koren = math.gcd(17, 22)
print(koren)


nakljucno = random.randint(5, 10)
nakljucno2 = random.randrange(6)

print(nakljucno)
print(nakljucno2)
"""
#Naloga napiši program, ki igra kamen škarje papir
#pravila so klasična; kamen premaga škarje, škarje premagajo papir, papir premaga kamen
#igra se do 2 točki
#zmagovalca ene točke preverjaj s funkcijo!
#ko eden izmed igralcev (racunalnik ali igralec) zmaga, napiši kdo je zmagal in 
#vprasaj igralca, če želi iti če eno igro.
#igralec odgovori z "y", ce hoce iti se eno, in z "n" ce noce.
#ce hoce iti se eno zani novo igro ampak si zapomni koliko iger je ze zmagal racunalnik
#in koliko igralec
#ce hoce zakljuciti zakljuci program

poteze = ["kamen", "skarje", "papir"]
potezeKode = [-3, 0, 2]

kamenAscii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papirAscii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

skarjeAscii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

risbe = [kamenAscii, skarjeAscii, papirAscii]

def gorDol():
  for i in range(5):
    if(i < 3):  
      print(i*"\n" + kamenAscii + "\n\n\n" + kamenAscii)
      time.sleep(0.3)
      os.system("cls")
    else:
      print((4-i)*"\n" + kamenAscii + "\n\n\n" + kamenAscii)
      time.sleep(0.3)
      os.system("cls")



def animiraj(potezaIgralec, potezaRačunalnik):
  #Prvi del animacije: samo 3x roki gor dol; začni v zgornji poziciji
  for i in range(3):
    gorDol()

  #Drugi del animacije: spremeni roko v pravo potezo
  risbaIgralec = risbe[poteze.index(potezaIgralec)]
  risbaRacunalnik = risbe[poteze.index(potezaRačunalnik)]

  for i in range(2):
    print(i*"\n" + kamenAscii + "\n\n\n" + kamenAscii)
    time.sleep(0.3)
    os.system("cls")
  print("\n\n" + risbaIgralec + "\n\n\n" + risbaRacunalnik)
  time.sleep(2)
  



def preveriZmagovalca(potezaIgralec, potezaRačunalnik): #oboje so številke, k = -3, š = 0, p = 2
  rezultat = potezaIgralec - potezaRačunalnik
  if(rezultat == 0):
    return 0 #izenačeno
  if(rezultat in [-3, -2, 5]):
    return 1 #prvi zmaga
  if(rezultat in [-5, 3, 2]):
    return 2 #drugi zmaga

def igraj(nasaPoteza):
  if(nasaPoteza in poteze):
    pozicija = poteze.index(nasaPoteza)
    potezaIgralec = potezeKode[pozicija]
    potezaRačunalnik = potezeKode[random.randint(0, 2)]

    os.system("cls")
    animiraj(nasaPoteza, poteze[potezeKode.index(potezaRačunalnik)])

    print("Tvoja poteza:  " + poteza)
    print("Računalnikova poteza:  " + poteze[potezeKode.index(potezaRačunalnik)])
    zmagovalec = preveriZmagovalca(potezaIgralec, potezaRačunalnik)
    return zmagovalec
  else:
    return -1


tockeRacunanik = 0
tockeIgralec = 0
zmaganeIgre = 0
izgubljeneIgre = 0

while(True):
  poteza = input("Vnesi svojo potezo! (kamen, skarje, papir):   ")
  rez = igraj(poteza)
  if(rez == -1):
    print("Neveljavna poteza!!")
  elif(rez == 0):
    print("Izenačeno!!")
  elif(rez == 1):
    print("Zmagal si!!")
    tockeIgralec += 1
  elif(rez == 2):
    print("Izgubil si!!")
    tockeRacunanik += 1

  print("\nTvoje tocke: " + str(tockeIgralec))
  print("Računalnikove tocke: " + str(tockeRacunanik)+"\n")

  if(tockeIgralec == 2):
    zmaganeIgre += 1
    odg = input("Zmagal si igro! Hočeš igrati ponovno?(y/n):   ")
    if(odg == "y"):
      tockeIgralec = 0
      tockeRacunanik = 0
      print("Rezultat:\n\tZmagane igre: " + str(zmaganeIgre) + "\n\tIzgubljene igre: " + str(izgubljeneIgre))
    else:
      print("Hvala za igro\nRezultat:\n\tZmagane igre: " + str(zmaganeIgre) + "\n\tIzgubljene igre: " + str(izgubljeneIgre))
      break
  elif(tockeRacunanik == 2):
    izgubljeneIgre += 1
    odg = input("Izgubil si igro! Hočeš igrati ponovno?(y/n):   ")
    if(odg == "y"):
      tockeIgralec = 0
      tockeRacunanik = 0
      print("Rezultat:\n\tZmagane igre: " + str(zmaganeIgre) + "\n\tIzgubljene igre: " + str(izgubljeneIgre))
    else:
      print("Hvala za igro\nRezultat:\n\tZmagane igre: " + str(zmaganeIgre) + "\n\tIzgubljene igre: " + str(izgubljeneIgre))
      break


#svitova kdeja: adventni koledar program