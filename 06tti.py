def tti(tomeg:float, magassag:float)->float:
    ttiadat=tomeg / pow(magassag,2)
    return ttiadat 

def tti_ertekeles(ttiadat:float)->str:
    if ttiadat<18.5:
        return "sovány"
    elif ttiadat>25:
        return "túlsúlyos"
    elif ttiadat<=0:
        return "tti indexe maghatározhatatlan"
    else:
        return "normális"  

nev=input("Adja meg a nevég:") 
testtomeg=float(input(f"Adja meg {nev} testtömegét:"))
magassag=float(input(f"Adja meg {nev} megasságát:"))

nevtti=tti(testtomeg,magassag)
nevertekeles=tti_ertekeles(nevtti)
print(f"{nev} tti indexe {nevtti}.")
print(f"{nev} {nevertekeles}.")
