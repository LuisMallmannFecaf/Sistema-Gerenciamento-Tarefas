import tkinter as tk
from tkinter import messagebox

# Cria a janela principal
janela = tk.Tk()
janela.title("Kanban de Tarefas")

# Define cores de fundo e fonte
cor_fundo = "#F0F0F0"
fonte = ("ARIAL", 12)

# Cria um quadro principal para os quadros Kanban
quadro_principal = tk.Frame(janela, bg=cor_fundo)
quadro_principal.pack()

# Inicia a interface gráfica
janela.mainloop()