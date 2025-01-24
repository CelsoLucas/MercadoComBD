from mostrar_estoque import ler_dados

def ver(ctk, tabview, conexao):

    for widget in tabview.tab("Estoque").winfo_children():
        widget.destroy()
    
    resultado = ler_dados(conexao)
    
    c1 = 0
    c2 = 1
    c3 = 2
    c4 = 3
    
    for item in resultado:
        ctk.CTkLabel(tabview.tab("Estoque"), text=f"ID: {item[c1]} | Produto: {item[c2]} | Preço: R${item[c3]:.2f} | Quantidade: {item[c4]}").pack()
        if c4 > len(resultado):
            c1 += 4
            c2 += 4
            c3 += 4
            c4 += 4
