import customtkinter as ctk
from adc_produto import adcProduto
from mostrar_estoque import mostrarEstoque

class abaEstoque():
    def __init__(self, tabview, conexao):
        self.conexao = conexao
        self.tab_estoque = tabview.add("Estoque")

        self.input_procurar_produtos = ctk.CTkEntry(self.tab_estoque, placeholder_text="Procurar Produtos", width=250)
        self.input_procurar_produtos.pack()
        self.input_procurar_produtos.place(x=510, y=10)

        self.btn_adicionar_produto = ctk.CTkButton(self.tab_estoque,text="+", width=25, height=25, corner_radius=100, command=lambda: self.tela_adc())
        self.btn_adicionar_produto.pack()
        self.btn_adicionar_produto.place(x=780, y=10)

        self.txt_estoque_global = ctk.CTkLabel(self.tab_estoque, text="")
        self.txt_estoque_global.pack()
        self.txt_estoque_global.place(x=50, y=50)

        mostrarEstoque(self.conexao, self.txt_estoque_global)

    def tela_adc(self):
        frame = ctk.CTkFrame(self.tab_estoque, width=800, height=800)
        frame.pack()
        frame.pack_propagate(False)

        txt_nome_produto = ctk.CTkLabel(frame, text="Nome do Produto")
        txt_nome_produto.pack(pady=10)

        input_nome_produto = ctk.CTkEntry(frame, placeholder_text="Nome do Produto")
        input_nome_produto.pack(pady=10)

        txt_preco_produto = ctk.CTkLabel(frame, text="Preço do Produto")
        txt_preco_produto.pack(pady=10)

        input_preco_produto = ctk.CTkEntry(frame, placeholder_text="R$")
        input_preco_produto.pack(pady=10)

        txt_quantidade_produto = ctk.CTkLabel(frame, text="Quantidade")
        txt_quantidade_produto.pack(pady=10)

        input_quantidade_produto = ctk.CTkEntry(frame, placeholder_text="Quantidade")
        input_quantidade_produto.pack()

        btn_adc_produto_estoque = ctk.CTkButton(frame, text="Adicionar ao Estoque", command=lambda: adcProduto(input_nome_produto.get(), input_preco_produto.get(), input_quantidade_produto.get(), frame, self.conexao, self.txt_estoque_global))
        btn_adc_produto_estoque.pack(pady=10)