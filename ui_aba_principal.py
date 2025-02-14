import customtkinter as ctk

class abaPrincipal():
    def __init__(self, tabview):
        self.tab_principal = tabview.add("Pagina Principal")

        self.frame_vendas_dia = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="red")
        self.frame_vendas_dia.pack_propagate(False)
        self.frame_vendas_dia.pack(pady=10)
        self.frame_vendas_dia.place(x=230, y=20)

        self.txt_vendas_dia = ctk.CTkLabel(self.frame_vendas_dia, text="Vendas do dia")
        self.txt_vendas_dia.pack()

        self.frame_vendas_semana = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="red")
        self.frame_vendas_semana.pack_propagate(False)
        self.frame_vendas_semana.pack(pady=10)
        self.frame_vendas_semana.place(x=510, y=20)
        
        self.txt_vendas_semana = ctk.CTkLabel(self.frame_vendas_semana, text="Vendas da Semana")
        self.txt_vendas_semana.pack()

        self.frame_vendas_mes = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="red")
        self.frame_vendas_mes.pack_propagate(False)
        self.frame_vendas_mes.pack(pady=10)
        self.frame_vendas_mes.place(x=790, y=20)
        
        self.txt_vendas_mes = ctk.CTkLabel(self.frame_vendas_mes, text="Vendas do dia")
        self.txt_vendas_mes.pack()

        self.frame_produtos_baixo_estoque = ctk.CTkFrame(self.tab_principal, width=810, height=250, fg_color="red")
        self.frame_produtos_baixo_estoque.pack_propagate(False)
        self.frame_produtos_baixo_estoque.pack(pady=10)
        self.frame_produtos_baixo_estoque.place(x=230, y=300)
        
        self.txt_produtos_baixo_estoque = ctk.CTkLabel(self.frame_produtos_baixo_estoque, text="Produtos com caixo Estoque")
        self.txt_produtos_baixo_estoque.pack()