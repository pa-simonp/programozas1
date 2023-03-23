# lower()
#A lower()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
# A szimbólumokat és számokat figyelmen kívül hagyja.

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)


#upper()
#A upper()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter nagybetűs.
# A szimbólumokat és számokat figyelmen kívül hagyja.

txt = "Hello my friends"

x = txt.upper()

print(x)

#capitalize()
#A capitalize()metódus egy karakterláncot ad vissza, ahol az első karakter nagybetű, a többi pedig kisbetű.

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


txt = "python is FUN!"

x = txt.capitalize()

print (x)




txt = "36 is my age."

x = txt.capitalize()

print (x)


#endswith()
#A endswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben False-t.

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)



txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)


txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)


#find()
#A find()metódus megkeresi a megadott érték első előfordulását.
#A find()metódus -1-et ad vissza, ha az érték nem található.
#A find()metódus szinte megegyezik a index() metódussal, csak annyi a különbség, hogy a index() metódus kivételt vet fel, ha nem található az érték. (Lásd a példát lent)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)


txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)



txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))




#isalnum()
#A isalnum()metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, azaz ábécé betűi (az) és számok (0-9).
#Példa olyan karakterekre, amelyek nem alfanumerikusak: (szóköz)!#%&? stb.

txt = "Company12"

x = txt.isalnum()

print(x)



txt = "Company 12"

x = txt.isalnum()

print(x)





#isalpha()
#A isalpha()metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (az).
#Példa olyan karakterekre, amelyek nem ábécé betűi: (szóköz)!#%&? stb

txt = "CompanyX"

x = txt.isalpha()

print(x)


txt = "Company10"

x = txt.isalpha()

print(x)

#islower()
#A islower()metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False-t.
#A számok, szimbólumok és szóközök nincsenek bejelölve, csak az ábécé karakterei.

txt = "hello world!"

x = txt.islower()

print(x)


a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())




#join()
#A join()metódus az összes elemet iterálhatóvá teszi, és egyetlen karakterláncba egyesíti.
#Elválasztóként egy karakterláncot kell megadni.

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)



#replace()
#A replace()metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre.

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)



txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)



txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)



#rfind()
#A rfind()metódus megkeresi a megadott érték utolsó előfordulását.
#A rfind()metódus -1-et ad vissza, ha az érték nem található.
#A rfind()módszer majdnem megegyezik a rindex() módszerrel. Lásd alább a példát.

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)



txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)



txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)


txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))


#rsrtip()
#A rstrip()metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter.

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")



txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)


#startswith()
#The startswith() method returns True if the string starts with the specified value, otherwise False.

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)



txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)

#strip()
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")



txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
