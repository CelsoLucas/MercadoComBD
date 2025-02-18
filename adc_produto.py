class adcProduto():
    def __init__(self, nome, preco, quantidade, conexao):
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"insert into estoque(nome, preco, quantidade) values ('{nome}', {preco}, {quantidade})"
        cursor.execute(comando)
        conexao.commit()
        cursor.close()


