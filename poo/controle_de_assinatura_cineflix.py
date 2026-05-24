class AssinanteCineflix:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        self.mensalidade_paga = True

    def atrasar_pagamento(self):
        self.mensalidade_paga = False

    def regularizar_pagamento(self):
        self.mensalidade_paga = True

    def autorizar_reproducao(self):
        if self.mensalidade_paga:
            return f"Acesso liberado. Bom filme, {self.nome}"
        else:
            return f"Acesso bloqueado {self.nome}. Por favor, regularize sua assinatura"


cliente1 = AssinanteCineflix("Mariana", "Família 4K")
print(cliente1.autorizar_reproducao())

cliente2 = AssinanteCineflix("Lucas", "Família 4K")
cliente2.atrasar_pagamento()
print(cliente2.autorizar_reproducao())
