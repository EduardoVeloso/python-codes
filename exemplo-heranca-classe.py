class Mamifero(object):
	def __init__(self, cor_de_pelo, genero, andar):
		self.cor_de_pelo = cor_de_pelo
		self.genero = genero
		self.num_de_patas = andar

	def falar(self):
		print("Olá sou um mamifero!")

	def andar(self):
		print("Estou andando sobre {} patas!".format(self.num_de_patas))
	
	def amamentar(self):
		if self.genero.lower()[0] == 'm' or self.genero.lower()[0] == "masculino":
			print("macho não amamenta!")
		else:
			print("Amamentando!")

class Pessoa(Mamifero):
	def __init__(self, cor_de_pelo, genero, andar, cabelo):
		Mamifero.__init__(self, cor_de_pelo, genero, andar)
		self.cabelo = cabelo
	
	def falar(self):
		#Mamifero.falar(self)
		print("Olá sou uma pessoa!")



Julia = Pessoa('preto','femea',2,'loiro')

print(Julia.cor_de_pelo)
Julia.falar()
Julia.andar()
print(Julia.genero)
Julia.amamentar()

print("===========================")

Rex = Mamifero("marrom", "masculino", 4)

Rex.falar()
Rex.andar()
print(Rex.genero)
Rex.amamentar()
