def checker(ctk, conexao, usuario_entry, senha_entry, janela_login):
    cursor = conexao.cursor()
    comando = f'SELECT * FROM usuarios WHERE usuario = "{usuario_entry}"'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    
    if not resultado:
        ctk.CTkLabel(janela_login, text="Usuário Inválido!").pack()
    else:
        usuario_db, senha_db = resultado[0][0], resultado[0][1]
        if senha_entry != senha_db:
            ctk.CTkLabel(janela_login, text="Senha Inválido!").pack()
        else:
            janela_login.destroy()

