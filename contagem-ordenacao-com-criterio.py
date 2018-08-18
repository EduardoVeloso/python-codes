def criar_intervalo(v):
	lista = []
	for i in range(len(v)):
		if v[i] % 3 == 2:
			lim_superior = v[i] + 1
			if v[i] - 2 == 0:
				lim_inferior = 1
			else:
				lim_inferior = v[i] - 1
			lista.append([lim_inferior,lim_superior])
		if v[i] % 3 == 1:
			lim_superior = v[i] + 2
			if v[i] == 1:
				lim_inferior = 1
			else:
				lim_inferior = v[i]
			lista.append([lim_inferior,lim_superior])
		if v[i] % 3 == 0:
			lim_superior = v[i]
			lim_inferior = v[i] - 2
			lista.append([lim_inferior,lim_superior])
	return lista

def remove_repetidos(vet):
    L = []
    for i in vet:
        if i not in L:
            L.append(i)
    return L

def retornar(v,lista):
	cont = 0
	j = 0
	while j < len(lista):
		for i in range(len(v)):
			if v[i] >= lista[j][0] and v[i] <= lista[j][1]:
				cont += 1
		print("Existem {} elementos na faixa de {} a {}".format(cont,lista[j][0],lista[j][1]))
		cont = 0		
		j +=1	
#Teste do código
v = [9,5,3,2,6,17,4,10,11,12]
v_final = remove_repetidos(sorted(criar_intervalo(v)))
retornar(v,v_final)
#complexidade n.m sendo n tamanho do vetor v
#e m o tamanho do vetor v_final, que contém os intervalos




