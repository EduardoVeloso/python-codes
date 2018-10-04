from criptografar_msg import criptografar
from descriptografar_msg import descriptografar

##########################################################################   
#                                                       MAIN                                                                               #
##########################################################################

while True:
    frase = str(input("Digite a frase(exit para sair): "))
    
    if frase == "EXIT" or frase == "exit":
        break
    vet_crip, b = criptografar(frase)
  
    print("----------------------------------------")
    print("Criptografado:")
    print((((((str(vet_crip)).replace(",", "")).replace("'","")).replace("[","")).replace("]","")))
    print("----------------------------------------")
    
    vet_descrip = descriptografar(vet_crip, b)
    print("Descriptografado:")
    print((((((str(vet_descrip)).replace(",", "")).replace("'","")).replace("[","")).replace("]","")))
    print("----------------------------------------")
    

    
