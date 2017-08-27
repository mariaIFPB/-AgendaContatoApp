from Pessoa import Pessoa
from Telefone import Telefone
import json
class Contato(Pessoa, Telefone):
    def __init__(self, criacao, listContato):
        super(Contato, self).__init__(nome, nascimento, email)
        super(Contato, self).__init__(numero, DDD, codPais)
        self.criacao = criacao
        self.listContato = listContato
        listContato = {nome : [ nascimento, email, numero, DDD, codPais ]}


    def ListarTelefones(self):
        pass