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
"""
json_data = json.loads(data)
>>> type(json_data)
<type 'dict'>
>>> print json_data.keys()
[u'telefones', u'ultimoNome', u'idade', u'primeiroNome', u'endereco', u'emails']

>>> arquivo = open('musica.txt', 'r')
>>> texto = arquivo.readlines()
>>> texto.append('Nova linha') 
>>> arquivo = open('musica.txt', 'w')
>>> arquivo.writelines(texto)
>>> arquivo.close()
"""