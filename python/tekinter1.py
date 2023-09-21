""" Crie uma janela usando a biblioteca TKINTER em Python que tenha um título "Sistema de Cadastro".
 Nesta janela, crie um campo de entrada de texto para o usuário digitar seu nome e um botão "Enviar" que, 
 ao ser clicado, exiba uma mensagem de boas-vindas com o nome do usuário em uma nova janela. 
 
 sua resposta"""

import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    nome = nome_entry.get()
    if nome:
        mensagem = f"Bem-vindo, {nome}!"
        messagebox.showinfo("Mensagem de Boas-vindas", mensagem)
    else:
        messagebox.showerror("Erro", "Por favor, digite um nome.")

janela = tk.Tk()
janela.title("Sistema de Cadastro")

nome_label = tk.Label(janela, text="Digite seu nome:")
nome_label.pack()

nome_entry = tk.Entry(janela)
nome_entry.pack()

enviar_button = tk.Button(janela, text="Enviar", command=exibir_mensagem)
enviar_button.pack()

janela.mainloop()
