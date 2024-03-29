#ord()
# A ord()függvény egy megadott karakter unicode kódját képviselő számot adja vissza.

x = ord("a")
print(x)

print(f"A nagy a betű kódja: {ord("A")}")  # 65

print(f"A kis a betű kódja: {ord("a")}") # 97





#chr()
# A chr()függvény a megadott unicode-ot képviselő karaktert adja vissza.

x = chr(97)

# min()
# A min()függvény a legalacsonyabb értékű elemet, vagy a legalacsonyabb értékű elemet adja vissza az iterációban.
# Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.

min(n1, n2, n3, ...)



# max()
# A max()függvény a legmagasabb értékű elemet, vagy a legmagasabb értékű elemet adja vissza az iterálható elemben.
# Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.

max(n1, n2, n3, ...)
vagy
max(iterable)


x = max("Mike", "John", "Vicky")



a = (1, 5, 3, 9)
x = max(a)


# list()
#A list()függvény egy lista objektumot hoz létre.
#A listaobjektum egy gyűjtemény, amely rendezett és változtatható.

x = list(('apple', 'banana', 'cherry'))



# index()
#A index()metódus megkeresi a megadott érték első előfordulását.
#A index()metódus kivételt jelent, ha az érték nem található.
#A index()metódus szinte megegyezik a find() metódussal, csak annyi a különbség, hogy a find() metódus -1-et ad vissza, ha nem található az érték. (Lásd a példát lent)

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)




txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)


txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))





