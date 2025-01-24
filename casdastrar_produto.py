def cadastrar_produto(nome, preco, quantidade, conexao):

    cursor = conexao.cursor()

    comando = f'INSERT INTO estoque (nome, preco, quantidade) VALUES ("{nome}", {preco}, {quantidade})'
    cursor.execute(comando)
    conexao.commit() 

    cursor.close()
