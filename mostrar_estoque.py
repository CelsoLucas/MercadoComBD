class mostrarEstoque():
    def __init__(self, conexao, txt_global):
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"select * from estoque"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()

        texto_estoque = ""
        for item in resultado:
            id_produto, nome, preco, quantidade = item  # Desempacotando a tupla corretamente
            texto_estoque += f"ID: {id_produto} | Nome: {nome} | Preço: R${preco:.2f} | Quantidade: {quantidade}\n"
        
        txt_global.configure(text=texto_estoque)