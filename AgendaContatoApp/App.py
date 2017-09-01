from DAgenda.Agenda import Agenda
from DContato.Contato import Contato
from DPessoa.Pessoa import Pessoa
from DTelefone.Telefone import Telefone
def main():
    try:
        Rodando = 1
        proprietario = input("informe o nome do proprietario: ")
        def menu():
    
            print("Seja Bem Vindo! \n opções: \n 1. Incluir um novo contato; \n 2. Listar todos os contatos;\n 3. Remover contato;\n 4. Buscar contato;\n 5. Informar a quantidade de contatos; \n 6. sair.")
            global opcao
            opcao = int(input("informe o numero da opção que você deseja executar:"))
            a = Agenda(proprietario)

            try:

                if (type(opcao) == str):
                    print("informe um inteiro, por favor.")

                if ((opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6) ):
                    print("opção invalida.")

            except:
                print("valores informados inválidos")

            if (opcao == 1):
                nome = input("informe o nome: ")
                nascimento = input("informe a data de nascimento: ")
                email = input("informe o email: ")
                numero = input("informe o numero de telefone: ")
                DDD = int(input("informe o DDD: "))
                codPais = int(input("informe o código do país: "))
                c = Pessoa(nome, nascimento, email)
                d = Telefone(numero, DDD, codPais)
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
    
        while (Rodando):
            menu()
            if (opcao == 6):
                Rodando = 0
    except:
        print("o programa está com um pequeno erro, contate o programador, por favor.")

if __name__ == "__main__":
    main()
