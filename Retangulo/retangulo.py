class Retangulo():
    def __init__(self):
        self.base = 0
        self.altura = 0
    def mudar_valores(self,new_base,new_altura):
        self.base = new_base
        self.altura = new_altura
    def retornar(self):
        return self.base,self.altura
    def calcula_area(self):
        return self.base*self.altura
    def calcula_perimetro(self):
        return 2*(self.base) + 2*(self.altura)