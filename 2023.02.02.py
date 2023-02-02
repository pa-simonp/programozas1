lista = [12, 5, 4, 8, 9, 11, 10, 13, 6]



def szelsoertek():
   min = lista[0]
   max = lista[0]
   for szam in lista:
       if szam < min:
           min = szam
       if szam > max:
           max = szam

print("A legkisebb szám a listában: ", min)
print("A legnagyobb szám a listában: ", max)

szelsoertek()