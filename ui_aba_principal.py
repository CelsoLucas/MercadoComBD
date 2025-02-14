import customtkinter as ctk

class abaPrincipal():
    def __init__(self, tabview):
        self.tab_principal = tabview.add("Pagina Principal")

        #frame vendas dia
        self.frame_vendas_dia = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="#ababab")
        self.frame_vendas_dia.pack_propagate(False)
        self.frame_vendas_dia.pack(pady=10)
        self.frame_vendas_dia.place(x=230, y=20)

        #texto vendas dia
        self.txt_vendas_dia = ctk.CTkLabel(self.frame_vendas_dia, text="", font=("poppins", 22))
        self.txt_vendas_dia.pack()

        #variavel global para inserir dados
        self.txt_vendas_dia_bd = ctk.CTkLabel(self.frame_vendas_dia, text="")
        self.txt_vendas_dia_bd.pack()

        #frame vendas semana
        self.frame_vendas_semana = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="#ababab")
        self.frame_vendas_semana.pack_propagate(False)
        self.frame_vendas_semana.pack(pady=10)
        self.frame_vendas_semana.place(x=510, y=20)
        
        #texto vendas semana
        self.txt_vendas_semana = ctk.CTkLabel(self.frame_vendas_semana, text="", font=("poppins", 22))
        self.txt_vendas_semana.pack()

        #variavel global para inserir dados
        self.txt_vendas_semana_bd = ctk.CTkLabel(self.frame_vendas_semana, text="")
        self.txt_vendas_semana_bd.pack()

        #frame vendas mes
        self.frame_vendas_mes = ctk.CTkFrame(self.tab_principal, width=250, height=250, fg_color="#ababab")
        self.frame_vendas_mes.pack_propagate(False)
        self.frame_vendas_mes.pack(pady=10)
        self.frame_vendas_mes.place(x=790, y=20)
        
        #texto vendas mes
        self.txt_vendas_mes = ctk.CTkLabel(self.frame_vendas_mes, text="", font=("poppins", 22))
        self.txt_vendas_mes.pack()

        #variavel global para inserir dados
        self.txt_vendas_mes_bd = ctk.CTkLabel(self.frame_vendas_mes, text="")
        self.txt_vendas_mes_bd.pack()

        #frame produtos com baixo estoque 
        self.frame_produtos_baixo_estoque = ctk.CTkFrame(self.tab_principal, width=810, height=250, fg_color="#ababab")
        self.frame_produtos_baixo_estoque.pack_propagate(False)
        self.frame_produtos_baixo_estoque.pack(pady=10)
        self.frame_produtos_baixo_estoque.place(x=230, y=300)
        
        #texto produtos com baixo estoque
        self.txt_produtos_baixo_estoque = ctk.CTkLabel(self.frame_produtos_baixo_estoque, text="", font=("poppins", 22))
        self.txt_produtos_baixo_estoque.pack()

        #variavel global para inserir dados
        self.txt_produtos_baixo_estoque_bd = ctk.CTkLabel(self.frame_produtos_baixo_estoque, text="")
        self.txt_produtos_baixo_estoque_bd.pack()