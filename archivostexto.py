a=open("principito.txt",'r')
print(a.read())

x=open("principito.txt",'a')
x.write("\n Principito el peor cuento")
print(a.read())


with open("principito.txt",'r') as texto:
    x=texto.read()
    linea=x.split()
    print(linea)
    print("De:",linea.count('de'))
    print("Desde:",linea.count('desde'))
    print("En:",linea.count('en'))
    print("Hacia:",linea.count('hacia'))
    print("Hasta:",linea.count('hasta'))
    print("Con:",linea.count('con'))
    print("Ante:",linea.count('ante'))
    print("Para:",linea.count('para'))
    print("Tras:",linea.count('tras'))
    print("Con:",linea.count('con'))




        
           


