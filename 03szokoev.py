ev=int(input("Adjon meg egy évet")) # legyen egynlő

if ev%4==0: # egyenlő-e
    if ev%100==0:
        if ev%400==0:
            print("igen")      
        else:
             print("nem")
    else:
        print("igen") 
else:
    print("nem")                    