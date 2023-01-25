#napisi program, ki izpise True ali False, odvisno od tega, ali je število, ki ga
#napisemo na input vecje ali manjse od 10

stevilo = input()

print(10 < int(stevilo)) #--> 10 < "7"

#int() --> pretvori iz česarkoli mu damo v številko
#str() --> pretvori iz česarkoli mu damo v besedo

#Napisi program, ki na inputu dobi stevilo in nato preveri ali je stevilo sodo ali liho
#izpisi True, ce je sodo in False, ce je liho

stevilo = int(input())
print(stevilo % 2 == 0)


#Napisi program, ki na vhodu dobi stevilo in potem izpise 
#"Ostanek pri deljenju tvojega stevila z 7 je x" (namesto x napisi ostanek)
stevilo = int(input())
ostanek = str(stevilo % 7)
print("Ostanek pri deljenju tvojega stevila z 7 je " + ostanek)
