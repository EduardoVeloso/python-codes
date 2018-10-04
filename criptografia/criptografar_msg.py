##########################################################################   
#                                              Func. Criptografar                                                                  #
##########################################################################
from random import randint

def criptografar(frase):
    b = randint(1,150)
    prim_novo = []    
#Primeira passada, somente criptografar caract. maiusc e minusc.
    for i in frase:
        a = str(i)
        if a.isupper() == True or a.islower() == True:
            prim_novo.append(chr(ord(i) + b))
        else:
            prim_novo.append(i)
            
#Segunda passada, inverter a frase
    seg_novo = prim_novo[::-1]
    
#Terceira passada, somente criptografar a partir da metade da frase
    terc_novo = seg_novo
    for i in range(len(seg_novo)//2, len(seg_novo)):
         terc_novo[i] = chr(ord(terc_novo[i]) - 1)
    return terc_novo, b
