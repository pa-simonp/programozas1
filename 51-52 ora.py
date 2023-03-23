
def honap(ho):
    if ho > 2 and ho <= 5 :
        return "Tavasz"
    elif ho > 5 and ho <=8 :
        return "Nyár"
    elif ho > 8 and ho <= 11 :
        return "Ősz"
    elif ho == 12 or (ho > 0 and ho <= 2) :
        return "Tél"
    else :
        return "Nincs ilyen hónap!"
tovabb=True
while (tovabb):
    ho=input("Adja meg hányadik hónap van:(1-12) ")
    if (ho != ""):
        ho = int(ho)
        print(honap(ho))
    else:
        tovabb = False
# Ez csak a teszteléshez kell, nem része a feladatnak.
print("Vége a programnak!")
