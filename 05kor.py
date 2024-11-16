x1=int(input("Adja meg az x koord:"))
y1=int(input("Adja meg az y koord:"))
r1=int(input("Adja meg a sugarat:"))

x2=int(input("Adja meg az x koord:"))
y2=int(input("Adja meg az y koord:"))
r2=int(input("Adja meg a sugarat:"))

a=int(input("Adja meg a pont x kord:"))
b=int(input("Adja meg a pont y kord:"))

pont_elso_korben = pow(x1-a,2)+pow(y1-b,2)<=r1**2
pont_masodik_korben = pow(x2-a,2)+pow(y2-b,2)<=r2**2

if not pont_elso_korben and not pont_masodik_korben:
    print("A pont egyik körlemezen sincs rajta.") 
elif pont_elso_korben and not pont_masodik_korben: 
    print("A pont csak az elsőként megadott körlemezen van rajta.")