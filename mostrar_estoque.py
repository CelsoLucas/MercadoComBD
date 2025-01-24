def ler_dados(conexao):

    cursor = conexao.cursor()
    comando = 'SELECT * FROM estoque'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    
    return resultado
