import customtkinter as ctk

class abaPdv():
    def __init__(self, tabview):
        self.tab_pvd = tabview.add("PDV")

        self.input_procurar_produtos = ctk.CTkEntry(self.tab_pvd, placeholder_text="Procurar Produtos", width=200)
        self.input_procurar_produtos.pack()

        