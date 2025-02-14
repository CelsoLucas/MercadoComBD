class sairConta():
    def __init__(self, conexao, parent):
        from tela_login import telaLogin
        self.conexao = conexao
        self.parent = parent
        self.parent.destroy()
        self.tela_login = telaLogin(self.conexao)
        self.tela_login.mainloop()