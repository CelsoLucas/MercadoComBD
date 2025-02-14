from tela_principal import telaPrincipal
class checker():
    def __init__(self, usuario, senha, validacao, conexao, tela_login):
        self.user = usuario
        self.senha = senha
        self.conexao = conexao
        cursor = self.conexao.cursor()
        comando = f"select nome_usu, senha from usuarios where nome_usu = '{self.user}'"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        cursor.close()
        if not resultado:
            validacao.configure(text="Usuario Invalido!")
        else:
            if self.senha != resultado[0][1]:
                validacao.configure(text="Senha Invalida!")
            else:
                validacao.configure(text=f"Bem Vindo {self.user}")
                tela_login.destroy()
                app = telaPrincipal(self.user, self.conexao)
                app.mainloop()