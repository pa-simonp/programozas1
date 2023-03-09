# Eljárás paraméter nélkül:
def koszont():
      print('Üdv 10. évfolyam')
koszont()

# Eljárás 1 parameter:
nev_globalis = "10.C" # nev1 - globális változó
def koszont_nevvel(nev):  # nev - formális paraméter
    print('Szia '+ nev +', üdv a fedélzeten!')  # nev - lokális változó
    print(f"Szia {nev}, üdv a fedélzeten!")
    print(f"Szia {nev_globalis}, üdv a fedélzeten!")
koszont_nevvel('Ádám')  # 'Ádám' - aktuális paraméter
# Eljárás 2 parameter:
def koszont_ket_nevvel(nev1, nev2):
    print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')
    print(f'Szia {nev1}, {nev2}\nÜdv a fedélzeten!')
koszont_ket_nevvel('Nóra', 'Ádám')

'''
Az argumentum (aktuális paraméter) lehet érték, kifejezés, változó is!
Az 'x', 'y' és 'eredmeny' nevű változók LOKÁLISAK, csak az eljáráson belül érhetők el! 
'''
def osszead(x, y):
    eredmeny = x + y
    print('A két szám összege: ', eredmeny)
osszead(10, 9)
osszead(5+5, 5+4)
a = 10
b = 9
osszead(a, b) 
    
# Az eljárás paramétere természetesen lehet összetett adattípus is:
def osszegzo(list):
    osszesen = 0
    for szam in list:
        osszesen = osszesen + szam
        print('A listában lévő számok összege: ', osszesen)
szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)