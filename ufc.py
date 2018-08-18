import random
import time 

class Lutador(object): 
	def __init__(self, nome, peso, altura, hp): 
		self.peso = peso 
		self.nome = nome
		self.altura = altura 
		self.hp = hp 
		self.default = hp 

	def __str__(self): 
		return self.nome 

	def atacar(self, other):
		dano = random.randint(0, 12) #variação do dano
		other.hp -= dano 
		return dano 	

class Luta(object): 

	def __init__(self, lutador1, lutador2): 
		self.desafiado = lutador1 
		self.desafiante = lutador2 
	
	def lutar(self): 
		lista = [self.desafiante, self.desafiado] 
		b = 0 
		while self.desafiado.hp >= 0 and self.desafiante.hp >= 0: 
			a = random.choice(lista) 
			for x in lista: 
				if x != a: 
					b = x 
					bn = a.atacar(b) 
					if bn == 0:
						print("\n{} atacou {} e causou {} de dano, soco de moça!!".format(a, b, bn))
						time.sleep(1)
					else:
						print("\n{} atacou {} e causou {} de dano".format(a, b, bn)) 
						time.sleep(1)
					if self.desafiado.hp == 0 or self.desafiante.hp == 0:
						break 
			
			if self.desafiado.hp > self.desafiante.hp:
				vencedor = self.desafiado.nome
				#perdedor = self.desafiante.nome
			else:
				vencedor = self.desafiante.nome
				#perdedor = self.desafiado.nome
		 
		print("\nO campeão foi {}!!! ".format(vencedor)) 

nome1 = input("Digite o nome do player 1: ")
nome2 = input("Digite o nome do player 2: ")
boxer1 = Lutador(nome1, 92, 1.75, 60) 
boxer2 = Lutador(nome2, 96, 1.64, 60) 
ufc = Luta(boxer1, boxer2) 
ufc.lutar()
