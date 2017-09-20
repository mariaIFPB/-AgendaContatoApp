from Model.Agenda import Agenda
from Model.Contato import Contato
from Model.Pessoa import Pessoa
from Model.Telefone import Telefone
from Model import Menu

def exibirMenu():
    print ("Seja Bem Vindo!\n"
        "opções:\n"
        "1. Incluir um novo contato;\n"
        "2. Listar todos os contatos;\n"
        "3. Remover contato;\n"
        "4. Buscar contato;\n"
        "5. Informar a quantidade de contatos;\n"
        "6. sair.")


def main():
    #try:
        Rodando = 1
        global opcao
        exibirMenu()
        proprietario = input("informe o nome do proprietario: ")
        opcao = int(input("informe o numero da opção que você deseja executar:"))
        a = Agenda(proprietario)

        try:

            if ((type(opcao) == str) or (type(opcao) == float)):
                print("informe um inteiro, por favor.")

            if ((opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6)):
                print("opção invalida.")

        except:
            print("valores informados inválidos")

        while (Rodando):
            if (opcao == 1):
                pessoa = Pessoa(nome, nascimento, email)
                pessoa.nome = input("informe o nome: ")
                pessoa.nascimento = input("informe a data de nascimento: ")
                pessoa.email = input("informe o email: ")
                tel = Telefone(numero, DDD, codPais)
                tel.numero = input("informe o numero de telefone: ")
                tel.DDD = int(input("informe o DDD: "))
                tel.codPais = int(input("informe o código do país: "))
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
                break

    #except:
        #print("o programa está com erros.")

if __name__ == "__main__":
    main()