from mostrar_estoque import mostrarEstoque
class adcProduto():
    def __init__(self, nome, preco, quantidade, frame, conexao, txt_global):
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"insert into estoque(nome, preco, quantidade) values ('{nome}', {preco}, {quantidade})"
        cursor.execute(comando)
        conexao.commit()
        cursor.close()
        mostrarEstoque(self.conexao, txt_global)
        frame.destroy()