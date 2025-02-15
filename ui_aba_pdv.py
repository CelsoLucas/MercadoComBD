import customtkinter as ctk
from procurar_produto import procurarProduto

class abaPdv():
    def __init__(self, tabview, conexao):
        self.tab_pvd = tabview.add("PDV")
        self.conexao = conexao

        self.input_procurar_produtos = ctk.CTkEntry(self.tab_pvd, placeholder_text="Procurar Produtos com id ou nome", width=200)
        self.input_procurar_produtos.pack()

        self.txt_variavel_global = ctk.CTkLabel(self.tab_pvd, text="")
        self.txt_variavel_global.pack()
        
        self.btn_menos = ctk.CTkButton(self.tab_pvd, text="-")
        self.btn_menos.pack()

        self.quant_global = ctk.CTkLabel(self.tab_pvd, text="")
        self.quant_global.pack()

        self.btn_mais = ctk.CTkButton(self.tab_pvd, text="+")
        self.btn_mais.pack()

        self.txt_quant_min_max_global = ctk.CTkLabel(self.tab_pvd, text="")
        self.txt_quant_min_max_global.pack()

        self.btn_procurar_produtos = ctk.CTkButton(self.tab_pvd, text="Buscar Produto", command= lambda: procurarProduto(self.conexao, self.input_procurar_produtos, self.txt_variavel_global))
        self.btn_procurar_produtos.pack()


        