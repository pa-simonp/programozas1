"""
nev = int(input("Kérek egy keresztnevet: "))
kor = int(input("Kérek egy életkort: "))

if kor < 1:
    print( nev "Csecsemő")

elif kor <= 6:
    print("Kisgyerek")

elif kor <= 12:
    print("Gyerek")

elif kor <= 16:
    print("Serdülő")

elif kor <= 25:
    print("Ifjú")

elif kor <= 65:
    print("Felnőtt")

elif kor > 65:
    print("Nyugdíjas")
"""


nev = input("Adja meg a keresztnevét: ")
kor = int(input("Adja meg az életkorát: "))

if kor < 1:
    print("A kora alapján", nev , "csecsemő!")

elif kor < 6:
    print("A kora alapján", nev , "Kisgyerek")

elif kor < 12:
    print("A kora alapján", nev , "Gyerek")

elif kor < 16:
    print("A kora alapján", nev , "Serdülő")

elif kor < 25:
    print("A kora alapján", nev , "Ifjú")

elif kor < 65:
    print("A kora alapján", nev , "Felnőtt")

else:
    print("A kora alapján", nev , "Nyugdíjas")


