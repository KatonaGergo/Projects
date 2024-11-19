aSzam = float(input("Írd be az első oldalát a háromszögnek!"))

bSzam = float(input("Írd be a második oldalát a háromszögnek!"))

cSzam = float(input("Írd be a harmadik oldalát a háromszögnek!"))

if aSzam + bSzam > cSzam and aSzam + cSzam > bSzam and cSzam + bSzam > aSzam:
    print("A háromszög megszerkeszhető!")

else:
    print("A háromszög nem szerkeszhető meg!")


#általános, szabályos, egyenlő szárú

if aSzam == bSzam and bSzam == cSzam:
    print("A háromszög szabályos.")
elif aSzam == bSzam or aSzam == cSzam or bSzam == cSzam:
    print("A háromszög egyenlő szárú.")
else:
    print("A háromszög általános háromszög.")


honap_szama=9
if honap_szama==1:
    print("Január")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
elif honap_szama==2:
    print("Február")
