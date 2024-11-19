import random

szelvenyem = []  #véletlen számokkal feltöltve

X = "dontetlen"

eredmeny = [1, 1, 2, 1, 1, X, 1, X, X, 2, X, X, X, 1]

talalatok_szama = ''

#hány döntetlen meccs




#találatok száma
for guess in range(len(eredmeny)):
    szelvenyem.append(random.choice(eredmeny))
    if szelvenyem in eredmeny:
        print("Eltaláltad!")
        talalatok_szama += 1
    
    elif szelvenyem[X] in eredmeny:
            szelvenyem.count[X]
            print()
    
    else:
        print("Nem talált!")

    


    


