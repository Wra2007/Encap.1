class Circulo:
    def _init_(self, radio):
        self.radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
            return 2*self.__pi*self.radio
        
    def calcularArea(self):
            return self.__pi*self.radio**2
            
c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"La constante PI es {c1.__pi}")