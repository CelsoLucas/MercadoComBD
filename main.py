import customtkinter as ctk
from tela_login import telaLogin
from tela_principal import telaPrincipal
import mysql.connector

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="suporte",
            password="suporte",
            database="mercado"
        )

        self.tela_login = telaLogin(self.conexao)
        self.tela_login.mainloop()

if __name__ == "__main__":
    app = Main()
    app.mainloop()
