class quantPDV():
    def __init__(self, aba_pdv):
        self.aba_pdv = aba_pdv

    def menos(self):
        if self.aba_pdv.quantidade == 0:
            self.aba_pdv.txt_quant_min_max_global.configure(text="Não pode diminuir mais")
        else:
            self.aba_pdv.quantidade -= 1
            self.aba_pdv.txt_quant_min_max_global.configure(text="")
        self.aba_pdv.atualizar_quantidade()

    def mais(self):
        self.aba_pdv.quantidade += 1
        self.aba_pdv.txt_quant_min_max_global.configure(text="")
        self.aba_pdv.atualizar_quantidade()
