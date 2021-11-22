class FormaBidimensional:
    
    lado=""
    altura =""

    def __init__(self):
        print("Criou uma forma")
    
    def perimetro (self):
        print("o perimetro é: ",self.lado*2 + self.altura*2)
    
    def area(self):
        print("a area é:", self.lado*self.altura)
    
class Cirulo(FormaBidimensional):
    raio=""

    def __init__(self):
        print("Criou um circulo")

    def perimetro(self):
        print("O perimetro do circulo é:" ,(self.raio*2)*3,14)
    
    def area(self):
        print("a area do circulo é: ", (self.raio**2)*3,14)
    
class Quadrado(FormaBidimensional):
    lado=""

    def __init__(self):
        print("criou um quadrado")

    def perimetro(self):
        print("o perimetro é: ",self.lado*4)
    
    def area(self):
        print("a area é: ", self.lado**2)

quadrado=Quadrado()
quadrado.lado= 4
quadrado.perimetro()
quadrado.area()
