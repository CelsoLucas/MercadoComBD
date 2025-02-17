import customtkinter as ctk
from procurar_produto import procurarProduto

class abaPdv():
    def __init__(self, tabview, conexao):
        self.tab_pdv = tabview.add("PDV")
        self.conexao = conexao
        
        self.input_procurar_produtos = ctk.CTkEntry(self.tab_pdv, placeholder_text="Procurar Produtos com id ou nome", width=220)
        self.input_procurar_produtos.pack()

        self.txt_resultado_busca = ctk.CTkLabel(self.tab_pdv, text="")

        self.quant_escolhida = ctk.CTkLabel(self.tab_pdv, text=0)

        self.txt_alerta_quant = ctk.CTkLabel(self.tab_pdv, text="")
        self.txt_alerta_quant.pack()
        self.txt_alerta_quant.place(x=750, y=60)

        self.produto = None

        self.btn_menos = ctk.CTkButton(self.tab_pdv, text="-", width=25, height=25, corner_radius=100, command=self.menos)
        self.btn_mais = ctk.CTkButton(self.tab_pdv, text="+",  width=25, height=25, corner_radius=100, command=self.mais)

        self.btn_procurar_produtos = ctk.CTkButton(self.tab_pdv, text="Buscar Produto", command=self.procurar_produto)
        self.btn_procurar_produtos.pack()
        self.btn_procurar_produtos.place(x=800)

    def procurar_produto(self):
        self.produto = procurarProduto(self.conexao, 
                                       self.input_procurar_produtos, 
                                       self.txt_resultado_busca,
                                       self.quant_escolhida,
                                       self.btn_menos, 
                                       self.btn_mais, 
                                       self.txt_alerta_quant)

    def menos(self):
        if self.produto:
            self.produto.menos()

    def mais(self):
        if self.produto:
            self.produto.mais()
