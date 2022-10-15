
# kérjünk be 2 számot (egész számot) utána írassuk ki az egész számot.
elso_szam=int(input("Kérek egy egész számot: "))
masodik_szam=int(input("Kérek egy másik számot: ")) 

"""
if   elso_szam > masodik_szam:
    print("Az első szám nagyobb." , elso_szam)

if elso_szam < masodik_szam:    
    print("A második szám nagyobb." , masodik_szam)
"""

if elso_szam > masodik_szam:
    print(elso_szam)

elif elso_szam < masodik_szam:
    print(masodik_szam)



else: 
    print("Az egyikszám megegyezik a másikkal.")        

