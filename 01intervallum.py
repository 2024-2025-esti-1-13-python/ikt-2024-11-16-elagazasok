# Intervallum bekérés
# Kérjen be egy intervallumot. Pl. "Adja meg az intervallum elejét" és "Adja meg az intervallum végét".
# "Az intervallum hibásan van megadva" hibaüzenetet írjon ki, ha a felhasználó által megadott intervallum 
# eleje nagyobb a végénél!

print("Intervallum bekérés")
eleje = int(input("Adja meg az intervallum elejét:"))
vege = int(input("Adja meg az intervallum végét:"))

if eleje>vege:
    print("Az intervallum hibásan van megadva")