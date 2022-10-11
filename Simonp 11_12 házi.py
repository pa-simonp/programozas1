egyikszam=int(input("kérek egy számot 1-100 között: "))
masikszam=int(input("kérek egy másik számot 1-100 között: "))
if egyikszam < egyikszam:
   print("Az második szám nagyobb.")
   print("Ennyivel: ", masikszam - egyikszam)
   
elif egyikszam > masikszam:
   print("Az első szám nagyobb.")
   print("Ennyivel: ", egyikszam - masikszam)

elif egyikszam == masikszam:
     print("Megegyezik")  



