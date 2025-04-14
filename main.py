import tkinter as tk
from tkinter import messagebox

# Cria a janela principal
janela = tk.Tk()
janela.title("Kanban de Tarefas")

# Define cores de fundo e fonte
cor_fundo = "#F0F0F0"
fonte = ("ARIAL", 12)

# Cria um quadro principal para os quadros Kanban
quadro_principal = tk.Frame(janela, bg='#000000')
quadro_principal.pack()

# Cria quadros para representar os estágios Kanban
quadro_a_fazer = tk.Frame(quadro_principal,height=100,borderwidth=2, relief=tk.SOLID)
quadro_a_fazer.pack(side=tk.LEFT, padx=20)
quadro_em_progresso = tk.Frame(quadro_principal,height=100, borderwidth=3, relief=tk.SOLID)
quadro_em_progresso.pack(side=tk.LEFT, padx=20)
quadro_concluido = tk.Frame(quadro_principal, height=100,borderwidth=3, relief=tk.SOLID)
quadro_concluido.pack(side=tk.LEFT, padx=20)

# Inicia a interface gráfica
janela.mainloop()