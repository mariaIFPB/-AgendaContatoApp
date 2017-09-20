import json

from Model.Telefone import Telefone
from Model.Pessoa import Pessoa

class Agenda:
    try:

        def __init__(self, proprietario, contatos = []):
            self.proprietario = proprietario
            self.contatos = contatos

        def __str__(self):
            return "Agenda[proprietario: %s, contatos: %s]" % (self.proprietario, self.contatos)

        def ContarContatos(self):
            contar = len(self.ctt)
            return(contar)

        def ListarContatos(self):
            for i in contatos:
                print(i)

        def IncluirContato(self):

            arquivoJson = open("listaContatos.json", "w", encoding="utf8")
            JsonObjs = json.loads(arquivoJson.read())
            pessoa = Pessoa(self.nome, self.nascimento, self.email)
            pessoaJson = {}
            pessoaJson["nome"] = pessoa.nome
            pessoaJson["nascimento"] = pessoa.nascimento
            pessoaJson["email"] = pessoa.email
            JsonObjs.append(pessoaJson)
            tel = Telefone(self.numero, self.DDD, self.codPais)
            t = open("telefones.json", "w")
            json.dump(tel, t)
            contatos = [{self.nome: {self.nascimento, self.email, self.tel}}]
            arquivoJson.write(contatos)
            json.dump(self.contatos, arquivoJson)
            arquivoJson.close()
            t.close()

        def ExcluirContato(self, remover):
            remover = remover.lower()
            for i in len(contatos):
                if remover == contatos[i]:
                    del(remover)

        def BuscarContatos(nome):
            nome = nome.lower()
            for i in len(contatos):
                if nome == contatos[i]:
                    return i
                else:
                    return("contato não encontrado")

    except:
        print("ocorreu um erro.")
