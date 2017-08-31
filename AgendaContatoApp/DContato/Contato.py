from DPessoa.Pessoa import Pessoa
from DTelefone.Telefone import Telefone
from datetime import date
import json

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
            t = open("telefones.json" "w")
            t.write(self.tel)
            t = open("telefones.json", "r")
            return (t.readlines())
            t.close()

    except:
        print("erro na classe contato.")
