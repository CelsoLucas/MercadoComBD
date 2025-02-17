import customtkinter as ctk
from ui_aba_principal import abaPrincipal
from ui_aba_pdv import abaPdv
from ui_aba_estoque import abaEstoque
from sair_conta import sairConta

class telaPrincipal(ctk.CTk):
    def __init__(self, usuario, conexao):
        super().__init__()
        self.conexao = conexao
        self.geometry("800x800")
        self.title("Mercado do Celso")

        self.grid_columnconfigure(0, weight=1, uniform="equal")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)

        self.txt_logo = ctk.CTkLabel(self, text="Celsadas Super Mercados", font=("poppins", 24))
        self.txt_logo.pack(fill="both", expand=True)
        self.txt_logo.place(x=50, y=20)

        self.txt_ola_user = ctk.CTkLabel(self, text=f"Olá, {usuario}", font=("poppins", 24))
        self.txt_ola_user.pack(pady=10)
        self.txt_ola_user.place(x=1500, y=20)

        self.btn_sair = ctk.CTkButton(self, text="Sair", font=("poppins", 24), command=lambda: sairConta(self.conexao, self))
        self.btn_sair.pack(pady=10)
        self.btn_sair.place(x=1700, y=20)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ctk.CTkTabview(self, width=1300, height=800, corner_radius=15)
        self.tabview.pack(pady=55)

        abaPrincipal(self.tabview)
        abaEstoque(self.tabview, self.conexao)
        abaPdv(self.tabview, self.conexao)

