class mostrarEstoque():
    def __init__(self, conexao):
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"select nome_usu, senha from usuarios where nome_usu = '{self.user}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()