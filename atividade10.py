n1= int (input("Digite seu primeiro numero"))
n2= int (input("Digite seu segundo numero"))
n3= int (input("Digite seu terceiro numero"))
if (n1 > n2 and n1 > n3):
    print(f"{n1} é o maior numero ")
elif(n2 > n1 and n2>n3):
    print(f"{n2} é o maior numero ")
else:
    print( F"{n3} é o maior numero")         