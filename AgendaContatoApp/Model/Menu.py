from Model.Agenda import Agenda
from Model.Contato import Contato
from Model.Pessoa import Pessoa
from Model.Telefone import Telefone

def menu():
    print("Seja Bem Vindo! \n opções: \n 1. Incluir um novo contato; \n 2. Listar todos os contatos;\n 3. Remover contato;\n 4. Buscar contato;\n 5. Informar a quantidade de contatos; \n 6. sair.")

    if (opcao == 1):
        proprietario = input("informe o nome do proprietario: ")
        a = Agenda(proprietario)
        pessoa = Pessoa(self.nome, self.nascimento, self.email)
        nome = input("informe o nome: ")
        nascimento = input("informe a data de nascimento: ")
        email = input("informe o email: ")
        numero = input("informe o numero de telefone: ")
        DDD = int(input("informe o DDD: "))
        codPais = int(input("informe o código do país: "))
        a.IncluirContato()

    if (opcao == 2):
        a.listarContatos()

    if (opcao == 3):
        remover = input(("informe qual o nome do contato que deseja remover: "))
        a.excluirContato(remover)

    if (opcao == 4):
        nome = input("informe o nome: ")
        a.BuscarContatos(nome)

    if (opcao == 5):
        a.ContarContatos()

    if (opcao == 6):
        print("programa finalizado.")