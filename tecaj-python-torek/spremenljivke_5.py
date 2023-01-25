#Besede
#Spremeljivka je lahko tudi beseda!

beseda = "to je beseda" #String of characters
print(beseda)

dolgStavek = "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."
print(dolgStavek)

cudnaBeseda = "%&#/)!/)( ß¤÷ 😼😏"
print(cudnaBeseda)

#Nalogica: v spremenljivko shrani stavek o tem kako se pocutis danes in ga izpisi
pocutje = "Danes me malo praska v grlu"
print(pocutje)

#sestevanje besed
prviDel = "vesel bozic"
drugiDel = "in srecno novo leto"
skupek = prviDel + " " + drugiDel
print(skupek)

#Nalogica izpisi z sestavljanjem besed "Zivjo ime mi je " plus vase ime

pozdrav = "Zivjo! ime mi je "
ime = "Niko"
print(pozdrav + ime)

print(ime * 4) # print(ime + ime + ime + ime)

#posebni znaki
#\n -> nova vrstica

vecVrstic = "poglej!\ntole je v novi vrstici"
print(vecVrstic)

#\t -> dolg presledek aka TAB
tab = "glej\tdolg presledek"
print(tab)


#Kratka nalogica
#bil/a si poreden/a v šoli in moraš 100 krat napisati "zelo bom priden/a"
#vsak stavek v svojo vrstico
#uprabi python in se izogni pisanju

kazenskaBeseda = "Zelo bom priden ;) \n"
kratSto = kazenskaBeseda * 100
print(kratSto)

#Ene par funkcij
a = type(True)
print(a)
b = input()
print(b)