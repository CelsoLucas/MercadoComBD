def restaurar_banco(conexao):
    cursor = conexao.cursor()

    comando = 'DROP TABLE estoque'
    cursor.execute(comando)
    conexao.commit() 

    comando = 'create table estoque(id int primary key auto_increment, nome varchar(20), preco float,quantidade int)'
    cursor.execute(comando)
    conexao.commit() 
    
    cursor.close()