from DContato.Contato import Contato
from DPessoa.Pessoa import Pessoa
from DTelefone.Telefone import Telefone
import json

class Agenda:
    try:

        def __init__(self, proprietario):
            self.proprietario = proprietario
            self.ctt = []
            self.tel = Telefone( self.numero, self.DDD, self.codPais)
            global ctt

        def ContarContatos(self):
            contar = len(self.ctt)
            return(contar)

        def ListarContatos(self):
            for i in len(ctt):
                print(i)

        def IncluirContato(self):

            t = open("telefones.json", "w")
            json.dump(tel, t)
            ctt = [{self.nome: {self.nascimento, self.email, self.tel}}]
            arquivoJson = open("listaContatos.json", "w")
            arquivoJson.write(ctt)
            json.dump(self.ctt, arquivoJson)
            arquivoJson.close()
            t.close()

        def ExcluirContato(self, remover):
            remover = remover.lower()
            for i in enumerate(ctt):
                if remover == ctt[i]:
                    del(remover)

        def BuscarContatos(nome):
            nome = nome.lower()
            for i in enumerate(ctt):
                if nome == ctt[i]:
                    return i
            return("contato não encontrado")

    except:
        print("ocorreu um erro.")
