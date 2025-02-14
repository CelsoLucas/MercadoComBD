import customtkinter as ctk
from ui_aba_principal import abaPrincipal

class telaPrincipal(ctk.CTk):
    def __init__(self, usuario):
        super().__init__()
        self.geometry("800x800")
        self.title("Mercado do Celso")

        self.txt_logo = ctk.CTkLabel(self, text="Celsadas Super Mercados", font=("poppins", 26))
        self.txt_logo.pack(pady=10)
        self.txt_logo.place(x=50, y=20)

        self.txt_ola_user = ctk.CTkLabel(self, text=f"Olá, {usuario}", font=("poppins", 26))
        self.txt_ola_user.pack(pady=10)
        self.txt_ola_user.place(x=1000, y=20)

        self.btn_sair = ctk.CTkButton(self, text="Sair", font=("poppins", 26))
        self.btn_sair.pack(pady=10)
        self.btn_sair.place(x=1200, y=20)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ctk.CTkTabview(self, width=1000, height=800, corner_radius=15)
        self.tabview.pack(pady=50)

        abaPrincipal(self.tabview)

usuario = "Celsadas"
if __name__ == "__main__":
    app = telaPrincipal(usuario)
    app.mainloop()