from Conta_Banco import ContaCorrente, CartaoCredito
from Agencia import Agencia, AgenciaVirtual, AgenciaComum, AgenciaPremium

#-----PROGRAMA -----:
#Criando primeira conta Corrente:
conta_Jean = ContaCorrente("Jean José Pereira da Silva", "000.000.000-00", 6483,82472)#Criando uma conta corrente

#Printando CPF e Nome do titular da conta
print(conta_Jean.cpf)
print(conta_Jean.nome)

#Consultando Saldo da conta
conta_Jean.Consultar_saldo()

#Depositando valor e consultando saldo após deposito
conta_Jean.Depositar_valor(1000)
conta_Jean.Consultar_saldo()

#Retirando valor e consultando saldo após retirada
conta_Jean.retirada_valor(500)
conta_Jean.Consultar_saldo()

#Verificando limite de crédito especial
conta_Jean.Consultar_LimiteChequeEspecial()

#Consultando histórico de transação
print(conta_Jean.Consultar_Historico_transacoes())

#Criando uma segunda conta corrente para receber transferencia da conta Jean:
conta_Jose = ContaCorrente("José", "111.111.111-11", 4822, 839372)
conta_Jean.transferir(600, conta_Jose) #Transferindo valor da conta Jean para conta José
conta_Jean.Consultar_saldo() #Consultando saldo após transação
conta_Jose.Consultar_saldo() #Consultando saldo após transação

#Consultando histórico de transação da conta José:
conta_Jose.Consultar_Historico_transacoes()

Cartao_Jean = CartaoCredito("Jean", conta_Jean) #Criando um cartão de crédito associado a conta Jean
print(Cartao_Jean.validade) #Printando validade do cartão
print(Cartao_Jean.numero) #Printando numero do cartão
print(Cartao_Jean.Cod_Seguranca) #Printando código de segurança do cartão

print(Cartao_Jean.__dict__) #Método que permite consultar em forma de dicionário todos os valores(atributos) de uma instância.

#-----------------------------------------------------------------------------------------#
print("-------------------------------------------------------------------------"*20) #Separando "tester" do arquivo Conta_Banco do arquivo Agencia
#Inicio programa:
#Criando uma agencia e verificando valor de caixa:
agencia1 = Agencia("(71)3267-6532", "00.000.000/0000-00", 1234)
agencia1.verificar_Caixa()

#Adicionando valor de caixa na agencia:
agencia1.caixa = 10000 #Adicionando R$10.000,00 ao caixa da empresa

#Realizando um emprestimo na agencia e consultando lista de emprestimos:
agencia1.emprestimo_Valor(600,"000.000.000-00",0.2)
print(agencia1.emprestimos)

#adiocando um cliente à agencia e verificando lista de clientes:
agencia1.adicionar_Clientes("Jean", "000.000.000-00", 10)
print(agencia1.cliente)

#Criando uma agencia vritual, verificando caixa, depositando um valor do caixa da agencia na caixa do paypal da agencia:
agenciavirtual1 = AgenciaVirtual("www.agenciavirtual1.com.br","(71)1111-1111","11.111.111/1111-11")
agenciavirtual1.verificar_Caixa()
agenciavirtual1.depositar_Paypal(100)
print(agenciavirtual1.caixa)
print(agenciavirtual1.caixa_paypal)

#Criando uma agencia comum e verificando caixa:
agenciacomum1 = AgenciaComum("(71)2222-2222", "22.222.222/2222-22")
agenciacomum1.verificar_Caixa()

#Criando uma agencia premium, verificando caixa e adicionando cliente:
agenciapremium1 = AgenciaPremium("(71)3333-33333", "33.333.3333/3333-33")
agenciapremium1.verificar_Caixa()
agenciapremium1.adicionar_Clientes("Jean","000000", 100)