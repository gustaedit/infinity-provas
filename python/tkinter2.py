""" Desenvolva uma calculadora simples utilizando a biblioteca Tkinter em Python.

A calculadora deve permitir a realização das operações básicas (adição, subtração, multiplicação e divisão) e ser capaz de lidar com entradas de números inteiros e decimais.

Além disso, a interface da calculadora deve ser intuitiva e fácil de usar para o usuário.


sua resposta """
import tkinter as tk

def atualizar_valor(valor):
    entrada_texto.delete(0, tk.END)
    entrada_texto.insert(tk.END, valor)

def calcular():
    try:
        expressao = entrada_texto.get()
        resultado = eval(expressao)
        atualizar_valor(resultado)
    except Exception as e:
        atualizar_valor("Erro")

def adicionar_digito(digito):
    entrada_atual = entrada_texto.get()
    entrada_texto.delete(0, tk.END)
    entrada_texto.insert(tk.END, entrada_atual + digito)

janela = tk.Tk()
janela.title("Calculadora")

entrada_texto = tk.Entry(janela, width=20, font=("Arial", 16))
entrada_texto.grid(row=0, column=0, columnspan=4)

botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for botao in botoes:
    tk.Button(
        janela,
        text=botao,
        width=5,
        height=2,
        font=("Arial", 16),
        command=lambda b=botao: adicionar_digito(b) if b != '=' else calcular()
    ).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

janela.mainloop()
