##########################################################################   
#                                         Func. Descriptografar                                                                 #
##########################################################################

def descriptografar(vet,b):
    for j in range(len(vet)//2, len(vet)):
         vet[j] = chr(ord(vet[j]) + 1)
    vet = vet[::-1]
    novo = []
    for i in vet:
        if i.isupper() ==True or i.islower() == True or ord(i) >= 123:
            novo.append(chr(ord(i) - b))
        else:
            novo.append(i)
    return novo
