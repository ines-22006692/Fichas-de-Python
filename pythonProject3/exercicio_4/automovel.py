class automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo


    def combustivel (self):

        return self.quantidade

    def autonomia (self):

        nrKm = (self.quantidade / self.consumo ) * 100

        return (int) (nrKm)

    def abastece(self, n_litros):

        quantidade = n_litros + self.quantidade

        if quantidade > self.capacidade:
            return ('Impossivel de abastecer')
        else:
            self.quantidade += n_litros
            return automovel.autonomia(self)

    def percorre(self, n_km):

        quantidade_gasta = (self.consumo / 100) * n_km
        if (n_km > automovel.autonomia(self)):
            return ('Trajecto não é efectuado')
        else:
            self.quantidade -= quantidade_gasta
            return automovel.autonomia(self)