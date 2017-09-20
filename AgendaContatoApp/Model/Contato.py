from datetime import date

from Model.Pessoa import Pessoa

from Model.Telefone import Telefone


class Contato():
    try:
        def __init__(self, pessoa):
            global criacao
            self.criacao = date.today()
            self.pessoa = pessoa
            self.pessoa = Pessoa(self.nome, self.nascimento, self.email)

            self.tel = Telefone( self.numero, self.DDD, self.codPais)

        def __str__(self):
            return ("data de criacao: " + criacao)

        def ListarTelefones(self):
            t = open("telefones.json", "w", encoding="utf8")
            t.write(self.tel)
            t = open("telefones.json", "r", encoding= "utf8")
            return (t.readlines())
            t.close()

    except:
        print("erro no contato.")
