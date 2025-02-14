import customtkinter as ctk
from check_login import checker

class telaLogin(ctk.CTk):
    def __init__(self, conexao):
        super().__init__()

        self.geometry("600x600")
        self.title("Login")

        txt_login = ctk.CTkLabel(self, text="LOGIN")
        txt_login.pack(pady=10)

        txt_user = ctk.CTkLabel(self, text="Usuario")
        txt_user.pack(pady=10)

        input_user = ctk.CTkEntry(self)
        input_user.pack(pady=10)

        txt_senha = ctk.CTkLabel(self, text="senha")
        txt_senha.pack(pady=10)

        input_senha = ctk.CTkEntry(self, show="*")
        input_senha.pack(pady=10)

        btn_login = ctk.CTkButton(self, text="Login", command=lambda: checker(input_user.get(), input_senha.get(), txt_validacao, conexao, self))
        btn_login.pack(pady=10)

        txt_validacao = ctk.CTkLabel(self, text="") 
        txt_validacao.pack(pady=10)

