from casdastrar_produto import cadastrar_produto
from tela_estoque import ver
def coletar_dados(ctk, tabview, conexao):

    def cadastrar():
        nome = input_nome.get()
        preco = input_preco.get()
        quant = input_quant.get()
        cadastrar_produto(nome, preco, quant, conexao)

        ver(ctk, tabview, conexao)

    nome_produto = ctk.CTkLabel(tabview.tab("Cadastrar Produto"), text="Nome")
    nome_produto.pack()

    input_nome = ctk.CTkEntry(tabview.tab("Cadastrar Produto"))
    input_nome.pack()

    preco_produto = ctk.CTkLabel(tabview.tab("Cadastrar Produto"),text="Preço")
    preco_produto.pack()

    input_preco = ctk.CTkEntry(tabview.tab("Cadastrar Produto"), placeholder_text="R$")
    input_preco.pack()
    
    quant_produto = ctk.CTkLabel(tabview.tab("Cadastrar Produto"), text="Quantidade")
    quant_produto.pack()

    input_quant = ctk.CTkEntry(tabview.tab("Cadastrar Produto"))
    input_quant.pack()

    btn_cadastrar = ctk.CTkButton(tabview.tab("Cadastrar Produto"), text="Cadastrar", command=cadastrar)
    btn_cadastrar.pack()