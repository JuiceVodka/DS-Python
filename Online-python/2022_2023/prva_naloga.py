#uporabnik vprasaj za stevilo, 
# ce to stevilo je deljivo s 5 napisi "deljivo s 5!", ce ni napisi "ni deljivo s 5 :("

#uporabnik vnese letnico, in program izpise ali to je prestopno leto (je prestopno / ni prestopno)
# deljiva s 4, niso deljiva s 100, razen, lahko so deljiva s 100 če so deljiva tudi s 400

print("[Deljivost s 5] Vnesi število: ")
stevilo = input()

if(stevilo[-1] == "5" or stevilo[-1] == "0"):
	print("JE!")

stevilo = int(stevilo)
if(stevilo % 5 == 0):
	print("deljivo s 5!")
else:
	print("ni deljivo s 5")


print("[Prestopno leto] Vnesi letnico")
leto = int(input())

if((leto % 4 == 0 and leto % 100 != 0) or (leto % 400 == 0)):
	print("Je prestopno")
else:
	print("Ni prestopno")

#uporabnik vnese temperaturo (v obliki stevilke)
#ce je nija od -273.15 napises "ni veljavna ker je pod absolutno niclo"
#ce je med -273.15 in 0 napišete "temperatura je pod lediščem"
#ce je 0 napisete "ledisce"
#ce je med 0 in 100 napiste "normalna temperatura"
#ce je 100 napisete vrelisce
#ce je nad 100 napisete "nad vreliscem"

temperatura = int(input("TEMPERATURA:  "))

if(temperatura < -273.15):
	print("ni veljavna ker je pod absolutno niclo")
elif(temperatura >= -273.15 and temperatura < 0):
	print("temperatura je pod lediščem")
elif(temperatura == 0):
	print("ledišče")
elif(temperatura > 0 and temperatura < 100):
	print("normalna temperatura")
elif(temperatura == 100):
	print("vrelisce")
elif(temperatura > 100):
	print("nad vreliscem")