"""
Tela de login com Tkinter e Custom Tkinter

By: George Telles
+55 11 93290-7425
"""

import customtkinter as ctk

def clique():
    print("Fazer Login")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Sistema de Login")
janela.geometry("500x300")

texto = ctk.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = ctk.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = ctk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

botao = ctk.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)



janela.mainloop()
