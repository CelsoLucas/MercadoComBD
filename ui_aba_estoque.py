import customtkinter as ctk
from adc_produto import adcProduto
from mostrar_estoque import mostrarEstoque
from tkinter import ttk, Scrollbar

class abaEstoque():
    def __init__(self, tabview, conexao):
        self.conexao = conexao
        self.tab_estoque = tabview.add("Estoque")

        self.input_procurar_produtos = ctk.CTkEntry(self.tab_estoque, placeholder_text="Procurar Produtos", width=250)
        self.input_procurar_produtos.pack()
        self.input_procurar_produtos.place(x=510, y=10)

        self.btn_adicionar_produto = ctk.CTkButton(self.tab_estoque, text="+", width=25, height=25, corner_radius=100, command=lambda: self.tela_adc())
        self.btn_adicionar_produto.pack()
        self.btn_adicionar_produto.place(x=780, y=10)

        self.frame_tabela = ctk.CTkFrame(self.tab_estoque)
        self.frame_tabela.pack(expand=True)
        
        self.scroll_tabela = Scrollbar(self.frame_tabela)
        self.scroll_tabela.pack(side="right", fill="y")

        columns = ("ID", "Nome", "Preço Un.", "Quantidade")
        self.tabela_estoque = ttk.Treeview(self.frame_tabela, columns=columns, show="headings", yscrollcommand=self.scroll_tabela.set)
        self.tabela_estoque.pack(expand=True)

        self.scroll_tabela.config(command=self.tabela_estoque.yview)

        # Configuração das colunas
        for col in columns:
            self.tabela_estoque.heading(col, text=col)
            self.tabela_estoque.column(col, width=100)

        self.tabela_estoque.column("ID", width=150)
        self.tabela_estoque.column("Nome", width=150)
        self.tabela_estoque.column("Preço Un.", width=150)
        self.tabela_estoque.column("Quantidade", width=150)

        # Inicialmente, chamar a função de atualizar a tabela
        self.atualizar_tabela_estoque()

    def atualizar_tabela_estoque(self):
        # Limpar a tabela antes de atualizar com novos dados
        for row in self.tabela_estoque.get_children():
            self.tabela_estoque.delete(row)
        
        # Preencher a tabela com os dados do banco de dados
        mostrarEstoque(self.conexao, self.frame_tabela, self.tabela_estoque)

    def tela_adc(self):
        self.frame_tabela.forget()  # Esconde a tabela de estoque
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

        btn_adc_produto_estoque = ctk.CTkButton(frame, text="Adicionar ao Estoque", command=lambda: 
                                                self.adicionar_produto(input_nome_produto.get(),
                                                                        input_preco_produto.get(),
                                                                        input_quantidade_produto.get(),
                                                                        frame))
        btn_adc_produto_estoque.pack(pady=10)
                
        input_nome_produto.delete(0, "end")
        input_preco_produto.delete(0, "end")
        input_quantidade_produto.delete(0, "end")

    def adicionar_produto(self, nome, preco, quantidade, frame):
        # Adiciona o produto ao banco de dados e atualiza a tabela
        adcProduto(nome, preco, quantidade, self.conexao)
        frame.destroy()  # Fecha a tela de adicionar produto
        self.atualizar_tabela_estoque()  # Atualiza a tabela de estoque
