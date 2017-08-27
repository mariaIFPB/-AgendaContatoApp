from DAgenda.Agenda import Agenda
from DContato.Contato import Contato
from DPessoa.Pessoa import Pessoa
from DTelefone.Telefone import Telefone
import json

def main():
    try:
        arquivoJson = open("listaContatos.json", "w")
        dadosJson = json.load(arquivoJson)

        def BuscarContatos(nome):
                for i in range(len(dadosJson)):
                    if nome == dadosJson[i]:
                        return i
                return None

        def menu():
            print("opções: \n 1. Incluir um novo contato;\n 2. Listar todos os contatos;\n 3. Remover contato;\n 4. Buscar contato;\n 5. Informar a quantidade de contatos \n 6. sair")

            opcao = int(input("informe o numero da opção que você deseja executar:"))

            if (opcao == 1):
                nome = input("informe o nome: ")
                dtNasc = input("informe a data de nascimento: ")
                email = input("informe o email: ")
                numero = input("informe o numero de telefone: ")
                DDD = int(input("informe o DDD: "))
                codPais = int(input("informe o código do país: "))
                incluirContato(contato)

            if (opcao == 2):
                listarContatos()

            if (opcao == 3):
                nome = input(("informe qual o nome do contato que deseja remover: "))
                excluir = excluirContato(nome)
                print(excluir)

            if (opcao == 4):
                nome = input("informe o nome: ")
                BuscarContatos(nome)

            if (opcao == 5):
                qtdContatos = ContarContatos()
                print(qtdContatos)

            if (opcao == 6):
                global programaRodando
                programaRodando = 0
                print("programa finalizado.")

            while (programaRodando):
                menu()
    except:
        print("o programa está com algum erro.")

if __name__ == "__main__":
    main()