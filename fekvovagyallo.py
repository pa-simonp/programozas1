m = int(input("Kérek egy magasságot: "))
sz = int(input("Kérek egy szélességet: "))

terület = m*sz

if sz < m:
    print("Álló téglalap, területe:" , terület)

elif sz > m:    
    print("Fekvő téglalap, területe:" , terület)

elif sz == m:
    print("Négyzet, területe:" , terület)    

