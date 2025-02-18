class mostrarEstoque():
    def __init__(self, conexao, frame, tabela):
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"select * from estoque"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()

        for item in resultado:
            id, nome, preco, quantidade = item  
            tabela.insert("", "end", values=(f"{id}", f"{nome}", f"{preco:.2f}", f"{quantidade}"))
        frame.pack(expand=True)
        tabela.pack(expand=True)

        
