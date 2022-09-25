def encripta(msg): 
    abc="abcdefghijklmñopqrstuwyzABCDEFGHIJKLMNÑOPRSTUWVXYZ0123456789"
    ran="qwertyuiopasdfghjklñzxcvbnmMNBVCXZÑLKJHGFDSAPOIUYTREWQ1357908642"
    msg_cif=""
    for x in msg:
        for n in range(len(abc)):
            if x==abc[n]:
                msg_cif+=ran[n]
    return msg_cif

def desencripta(msg): 
    abc="abcdefghijklmñopqrstuwyzABCDEFGHIJKLMNÑOPRSTUWVXYZ0123456789"
    ran="qwertyuiopasdfghjklñzxcvbnmMNBVCXZÑLKJHGFDSAPOIUYTREWQ1357908642"
    msg_cif=""
    for x in msg:
        for n in range(len(ran)):
            if x==ran[n]:
                msg_cif+=abc[n]
    return msg_cif

msg=input("Ingrese el texto para encriptar")
msg_cif=encripta(msg)
print(msg)
print(msg_cif)
print(desencripta(msg_cif))
