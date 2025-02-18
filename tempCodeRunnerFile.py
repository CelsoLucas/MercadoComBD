import customtkinter as ctk
from tela_login import telaLogin
import mysql.connector

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="celsadas",
            password="33880188",
            database="mercado"
        )

        self.tela_login = telaLogin(self.conexao)
        self.tela_login.mainloop()

        self.conexao.close()
        
if __name__ == "__main__":
    app = Main()
    app.mainloop()
