#seznam najljubsih stvari (sproti izgradimo)

#Naredi spremeljivko tipa seznam, in v kodi s funkcijami append 
#daj vanj 5 katerihkoli stvari, ki so ti vsec
#na koncu seznam izpiši

seznam = []
seznam.append("kosarka")
seznam.append("programiranje")
seznam.append("kitara")
seznam.append("igrice")
seznam.append("plezanje")
print(seznam)

#Uporabnik sedaj vsene 5 stvari (vsako posebaj), in nato se vse te tudi dodajo v seznam
#na koncu spet izpisi seznam

seznam.append(input())
seznam.append(input())
seznam.append(input())
seznam.append(input())
seznam.append(input())

print(seznam)

#Napisi program, ki mu vneseš katerega meseca si se rodil, in ti program pove kaj si po
#horoskopu
#pri tem uporabi seznam v katerem so shranjeni vsi horoskopi

mesec = int(input())

horoskopi = ["kozorog", "vodnar", "riba", "oven", "bik", "dvojcka", "rak", "lev", "devica", "tehtnica", "skorpijon", "strelec"]
znamenje = horoskopi[mesec -1]
print("Po horoskopu si " + znamenje)

#Napisi program, ki mu vneseš na katero leto si rojen, in ti program napise,
# kaj si po kitajskem horoskopu
#pri tem uporabi seznam kjer so shranjeni kitajski horoskopi

kitajski_horoskopi = ["podgana", "bivol", "tiger", "zajec", "zmaj", "kača", "konj", "koza", "opica", "petelin", "pes", "prašič"]

leto = int(input())

print(kitajski_horoskopi[leto % 12 - 4])


#if stavki