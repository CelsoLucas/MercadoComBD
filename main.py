import mysql.connector
import customtkinter as ctk
from tela_cadastrar_produto import coletar_dados
from restaurar_bd import restaurar_banco
from tela_login import user_login

def main():

    conexao = mysql.connector.connect(
        host='localhost',
        user='suporte',
        password='suporte',
        database='mercado'
    )
    
    user_login(ctk, conexao)

    restaurar_banco(conexao)
    
    janela = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    janela.geometry("500x500")
    
    tabview = ctk.CTkTabview(janela)
    tabview.pack()
    tabview.add("Cadastrar Produto")
    tabview.add("Estoque")
    tabview.add("Vender")
    tabview.add("Cadastrar Funcionario")

    coletar_dados(ctk, tabview, conexao)

    janela.mainloop()
    conexao.close()

if __name__ == "__main__":
    main()


