class Balde:
    capacidade = ""
    volume = ""
    def __init__(self):
        print("criou balde")
    
    def encher(self, vol):
            if(self.volume + vol > self.capacidade):
                return "nao transborde o balde"
            else:
                self.volume=self.volume+vol
                return self.volume   
    def esvaziar(self,vol):
        if(self.volume - vol > 0 ):
            self.volume = self.volume-vol
            return( self.volume)
        else:
            return "não tem agua suficiente no balde"        
    
   
balde1 = Balde()
balde1.capacidade= 10
balde1.volume = 0
print(balde1.encher(11))
balde1.encher(10)
print(balde1.esvaziar(9))



balde2 = Balde()
balde2.capacidade=20
balde2.volume=10
print(balde2.encher(7))
print(balde2.esvaziar(19))

