from retangulo import Retangulo

comprimento = float(input("Digite o valor do comprimento do local: "))
largura = float(input("Digite o valor da largura do local: "))

piso = Retangulo()

lag_piso = float(input("Digite a largura do piso "))
com_piso = float(input("Digite o comprimento do piso "))

piso.mudar_valores(lag_piso,com_piso)
area_total = largura*comprimento
num_pisos = area_total / piso.calcula_area()

print(num_pisos)

