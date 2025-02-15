class procurarProduto():
    def __init__(self, conexao, pesquisa, txt_global):
        self.conexao = conexao
        self.pesquisa = pesquisa.get().strip()

        cursor = self.conexao.cursor()

        if self.pesquisa.isdigit():
            self.pesquisa = int(self.pesquisa)
            comando = f"select nome, preco, quantidade from estoque where id = {self.pesquisa}"
        else:
            self.pesquisa = str(self.pesquisa)
            comando = f"select nome, preco, quantidade from estoque where nome = '{self.pesquisa}'"

        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()

        texto_estoque = ""
        for item in resultado:
            nome, preco, self.quant = item
            texto_estoque += f"{nome}   R${preco:.2f} un."
        
        txt_global.configure(text=texto_estoque)
        btn_menos.pack()
        txt_quant.pack()
        btn_mais.pack()


