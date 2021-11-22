class ContaBancaria :
    nome=""
    saldo=""
    numero=""

    def __init__(self):
        print("criou a conta")
    def depositar(self,din):
        self.saldo= self.saldo + din

    def sacar(self,din):
        if self.saldo - din<0:
            print("Estorou o saldo")
        else:
            self.saldo=self.saldo-din

class ContaCorrente(ContaBancaria):

    def PagarBoleto(self,Boleto):
        if self.saldo - Boleto < 0:
            print("Saldo insuficiente")
        else:
            self.saldo=self.saldo - Boleto
            print("boleto pago")

class ContaPoupanca(ContaBancaria):
    taxa=""

    def __init__(self):
        self.taxa=0
    def resgatar(self,valor):
        if(valor>self.taxa):
            self.saldo=valor-self.taxa
        else:
            print("não há valor suficiente na poupança")

class ContaInvestimento(ContaBancaria):
    consultor=""


    def resgatar(self,valor):
        self.saldo=self.saldo+valor

