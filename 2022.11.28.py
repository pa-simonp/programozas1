"""
    print("1. verzió")
szam > 0
for _ in range(100):

szam = szam + 1
print(szam,end=" ")
print()



print("2. verzió")
szam = 1
for _ in range(100):
    print(szam,end=" ")
    szam = szam + 1
print()    


print("3. verzió")
szam = 0
for _ in range(1,101):
    szam = szam + 1
    print(szam,end=" ")
print()


print("4. verzió")
szam = 0
for _ in range(1,101,1):
    szam = szam + 1
    print(szam,end=" ")
print()    



print("5.verzió")
szam = 0
for _ in range(5,105.1):
    szam = szam + 1
    print(szam,end=" ")
print()


print("6.verzió")
for szam in range(100):
    print(szam + 1,end=" ")
print()    
for i in range(50,101,3):
    print(i)


for i in range(50,101,3):
    print(i,end=" ")

for i in range(50,101,3):
    print(szam,end=" ")
print()
"""
"""

for szam in range(50,101,3):
    if szam % 2 == 0:
        print(szam,end=" ")




szoveg="Hello world!"
for kar in szoveg:
    print(kar,end="")


szoveg = input("Kérem a nevedet:")
for kar in szoveg:
    print(kar,end=" ")

szoveg = input("Kérem a nevedet:")
for kar in szoveg:
    print(kar.upper(),end=" ")
"""

szamlalo = 0
nev = input("Kérem a teljes nevedet kisbetűvel:")
for kar in nev:
    if szamlalo == 0:
       print(kar.upper(),end="")
    else:
    print(kar,end=" ")
    #print(szamlalo,end=" ")
    szamlalo += 1