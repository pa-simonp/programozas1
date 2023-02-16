
lista1 = [3, 12, 3, 4, 7, 15, 1]
lista2 = [2, 4, 6, 3, 12]
lista3 = [2, 4, 7, 8]

def oszzegzes_tetele(lista_oszegzes):
    osszesen = 0
    for szam in lista_osszegzes:
	      osszesen = osszesen + szam

    print("A listában található összege: ", osszesen)

def eldontes_tetele(lista_eldontes):

    talalat = False
    index = 0
    while index < len(lista_eldontes) and not talalat:
	      if lista_eldontes[index] % 3 == 0:
		        talalat = True
	      index = index + 1

    print('A hárommal osztható szám indexe a listában: ', index-1)
    


oszzegzes_tetele(lista1)
oszzegzes_tetele(lista2)    
oszzegzes_tetele([10, 20, 30]) 
eldontes_tetele(lista3)