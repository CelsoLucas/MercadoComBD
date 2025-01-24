from check_user import checker

def user_login(ctk, conexao):
    janela_login = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela_login.geometry("500x500")

    texto1 = ctk.CTkLabel(janela_login, text="Usuario").pack()
    user_entry = ctk.CTkEntry(janela_login)
    user_entry.pack()

    texto2 = ctk.CTkLabel(janela_login, text="Senha").pack()
    senha_entry = ctk.CTkEntry(janela_login, show="*")
    senha_entry.pack()

    def login():
        usuario = user_entry.get().strip()
        senha = senha_entry.get().strip()

        checker(ctk, conexao, usuario, senha, janela_login)
    
    ctk.CTkButton(janela_login, text="Cadastrar", command=login).pack()
    

    janela_login.mainloop()