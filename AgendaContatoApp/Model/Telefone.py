class Telefone():
    try:

        def __init__(self, numero, DDD, codPais):
            self.numero = numero
            self.DDD = DDD
            self.codPais = codPais

        def __str__(self):
            return ("+ %i ( %i )%s" % self.codPais, self.DDD, self.numero)


    except:
        print("erro na classe Telefone")
