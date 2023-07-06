from Conta_Banco import ContaCorrente, CartaoCredito
from random import randint
class Agencia:#Criação de uma classe de agencia
    def __init__(self, telefone, cnpj, numero): #Definindo o método inicial
        self.telefone = telefone #Telefone da agencia que será atribuido quando criada
        self.cnpj = cnpj #CNPJ da agencia que será atribuido quando criada
        self.numero = numero #Numero da agencia que será atribuido quando criada
        self.cliente = [] #Lista de Clientes da agencia
        self.caixa = 0 #Valor em caixa definido inicialmente como zero
        self.emprestimos = [] #Lista de emprestimos realizados pela agencia

    def verificar_Caixa(self): #Verificador de saúde financeira da agencia
        if self.caixa < 100000:
            print("Valor em caixa é de R${:,.2f}. Valor abaixo do valor minimo necessário.".format(self.caixa))
        else:
            print("Valor em caixa é de R${:,.2f}. Valor dentro dos padrões de recursos necessários." .format(self.caixa))

    def emprestimo_Valor(self, valor, cpf, juros): #Método de realização de emprestimo pela agencia
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf, juros)) #Adicionando à lista de emprestimo uma tupla contendo o valor dele, o cpf da pessoa e o juros.
        else:
            print("Emprestimo negado. Valor em caixa insuficiente")

    def adicionar_Clientes(self, nome, cpf, patrimonio): #adicionando um cliente à agencia
        self.cliente.append((nome, cpf, patrimonio)) #Adicionando à lista de cliente uma tupla contendo o nome dele, o cpf da pessoa e o seu patrimonio.


class AgenciaVirtual(Agencia): #Criando uma subclasse da classe agencia , que vai ter os mesmo atributos da classe Agencia e também seu atributos especificos
    def __init__(self, site, telefone, cnpj): #Definindo os atriutoss inicias da subclasse agencia virtual
        self.site = site
        super().__init__(telefone,cnpj,1000) #"Chamando" os atributos inicias da classe Agencia. Classe "Mãe".
        self.caixa = 1000000 #Determinando que quando agencia virtual for criada ela já possua um caide um milhão de reais
        self.caixa_paypal = 0 #Inicialmente valor do caixa do paypal é zero

    def depositar_Paypal(self, valor): #Realizando uma transferencia do caixa da agencia para o caixa do Paypal da agencia
        if valor <= self.caixa:
            self.caixa -= valor
            self.caixa_paypal +=valor
        else:
            print("Valor indisponivel para esta transação")

    def retirar_Paypal(self, valor): #Realizando uma transferencia do caixa do Paypal da agencia para o caixa da agencia
        if self.caixa_paypal >= valor:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print("Valor indisponivel para esta transação")




class AgenciaComum(Agencia): #Criando uma agencia comum
    def __init__(self,telefone,cnpj):
        super().__init__(telefone, cnpj,numero = randint(1001, 9999)) #Colocando para o numro da agencia ser gerada aleatoriamente ao ser criada. Herdando atributos iniciais da classe Agencia.
        self.caixa = 1000000


class AgenciaPremium(Agencia): #Criando agencia premium
    def __init__(self,telefone,cnpj):
        super().__init__(telefone, cnpj,numero = randint(1001, 9999)) #Colocando para o numro da agencia ser gerada aleatoriamente ao ser criada
        self.caixa = 10000000

    def adicionar_Clientes(self, nome, cpf, patrimonio): #Modificando a forma como o méotodo herdado da classe Agencia funciona para subclasse Agencia Premium. Polimorfismo.
        if patrimonio > 100000: #Cliente precisa ter mais d eum milhão de patrimonio para se torna cliente premium.
            super().adicionar_Clientes(nome,cpf,patrimonio) #
        else:
            print("Cliente não possue patrimonio suficiente para se torna cliente premium.")




