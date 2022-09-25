def voc(x):
    a=e=i=o=u=0
    for x in frase:
        if x in "a":
            a=a+1
        elif x in "e":
            e=e+1
        elif x in "i":
            i=i+1
        elif x in "o":
            o=o+1
        elif x in "u":
            u=u+1
    print("Vocales de a:",a)
    print("Vocales de e:",e)
    print("Vocales de i:",i)
    print("Vocales de o:",o)
    print("Vocales de u:",u)
    
frase=input("Ingrese el texto:")
voc(frase)
