a=int(input("kérem az első számot 1-100 között:  "))
b=int(input("kérek egy második számot 1-100 között:  "))
c=input("kérek egy müveletett: ")
if  c=="+":
    print("A két szám összege: ",(a+b))

if c=="-":
    print("A két szám különbsége: " ,(a-b))

elif c=="*":
    print("A két szám szorzata: " ,(a*b))