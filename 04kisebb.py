szam1=int(input("Adj meg egy számot! "))
szam2=int(input("Adj meg egy másik számot! "))

if szam1<szam2:
    print(f"A kisebb érték {szam1}")
elif szam2<szam1:
    print(f"A kisebb érték {szam2}")
else:
    print("A két szám egyenlő.")