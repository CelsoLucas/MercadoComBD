import customtkinter as ctk

class procurarProduto():
    def __init__(self, conexao, pesquisa, txt_resultado, txt_quant_escolhida, btn_menos, btn_mais, txt_alerta):
        self.conexao = conexao
        self.pesquisa = pesquisa.get().strip()
        cursor = self.conexao.cursor()
        self.cont = 0
        self.txt_quant_escolhida = txt_quant_escolhida
        self.txt_alerta = txt_alerta
        self.quant = 0

        if self.pesquisa.isdigit():
            self.pesquisa = int(self.pesquisa)
            comando = f"select nome, preco, quantidade from estoque where id = {self.pesquisa}"
        else:
            self.pesquisa = str(self.pesquisa)
            comando = f"select nome, preco, quantidade from estoque where nome = '{self.pesquisa}'"

        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()

        if not resultado:
            txt_resultado.configure(text="Nenhum produto encontrado!")
            txt_resultado.pack()
            txt_resultado.place(x=550, y=50)
        else:
            texto_estoque = ""
            for item in resultado:
                nome, preco, self.quant = item
                texto_estoque += f"{nome}   R${preco:.2f} un."
            
            txt_resultado.configure(text=texto_estoque)
            txt_resultado.pack()
            txt_resultado.place(x=550, y=50)

            btn_menos.pack()
            btn_menos.place(x=750, y=50)

            self.txt_quant_escolhida.pack()
            self.txt_quant_escolhida.place(x=790, y=50)

            btn_mais.pack()
            btn_mais.place(x=810, y=50)

    def menos(self):
        if self.cont > 0:
            self.cont -= 1
            self.txt_quant_escolhida.configure(text=f"{self.cont}")
        else:
            self.txt_alerta.configure(text="Não pode diminuir mais")

    def mais(self):
        if self.cont < self.quant:
            self.cont += 1
            self.txt_quant_escolhida.configure(text=f"{self.cont}")
        else:
            self.txt_alerta.configure(text="Não pode aumentar mais")
