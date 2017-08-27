import json
from Contato import Contato

class Agenda(Contato):
    try:
        arquivoJson = open("listaContatos.json", "w")
        dadosJson = json.load(arquivoJson)

        def __init__(self, proprietario):
            self.proprietario = proprietario

        def ContarContatos(self):
            contar = len(dadosJson)
            print(contar)

        def ListarContatos(self):
            dadosJson.readlines()

        def IncluirContato(self, Contato):
            contatos[contato] = [pessoa, telefone]

        def ExcluirContato(self, nome):
            pass
    except:
        print("erro na classe agenda")
