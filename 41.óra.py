"""
napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]

osszesen = 0
for ertekesites in napi_ertekesitesek:
        osszesen = osszesen + ertekesites

print("A héten ennyi értékesítés történt: ", osszesen)
print(f"A héten ennyi értékesítés történt:  {osszesen}")



print('Ez a program kiszámolja az átlagodat.')
print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
print('--------------------------------------------')

darab = 0
osszeg = 0

erdemjegy = int(input('Add meg az első érdemjegyet: '))
while erdemjegy != 0:
        darab = darab + 1
        osszeg = osszeg + erdemjegy
        erdemjegy = int(input('Add meg az következő érdemjegyet: '))

if darab != 0:
        print('A jegyeid átlaga: ', osszeg / darab)
else:
        print('Nem adtál meg egy jegyet sem!')


lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')
  
"""

lista = ['kék', 'zöld', 'piros', 'fehér']

talalat = False
index = 0
while index < len(lista) and not talalat:
        if lista[index] == 'piros':
            talalat = True
        index = index + 1

if talalat:
        print('Van a listában piros szín, az indexe: ', index-1)
else:
        print('Nincs a listában piros szín.')
