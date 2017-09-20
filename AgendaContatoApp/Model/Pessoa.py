class Pessoa():
    try:
        def __init__(self, nome, nascimento, email):
            self.nome = nome
            self.nascimento = nascimento
            self.email = email

        def __str__(self):
            return "%s , %s , %s" % (self.nome + self.nascimento + self.email)
    except:
        print("erro na classe Pessoa.")
