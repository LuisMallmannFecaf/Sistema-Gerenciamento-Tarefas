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

# Cria quadros para representar os estágios Kanban
quadro_a_fazer = tk.Frame(quadro_principal,borderwidth=2, relief=tk.SOLID)
quadro_a_fazer.pack(side=tk.LEFT, padx=20)
quadro_em_progresso = tk.Frame(quadro_principal, borderwidth=3, relief=tk.SOLID)
quadro_em_progresso.pack(side=tk.LEFT, padx=20)
quadro_concluido = tk.Frame(quadro_principal, borderwidth=3, relief=tk.SOLID)
quadro_concluido.pack(side=tk.LEFT, padx=20)

# Define cores para os quadros Kanban e suas bordas
cor_a_fazer = "#ff0000" # VERMELHO
cor_em_progresso= "#FFFF00" # AMARELO
cor_concluido = "#98FB98" # VERDE

# Adiciona rótulos para identificação dos quadros Kanban
label_a_fazer = tk.Label(quadro_a_fazer, text="A fazer",width=26, height=3,font=fonte, bg=cor_a_fazer,borderwidth=2,relief=tk.SOLID)
label_a_fazer.pack()
label_em_progresso = tk.Label(quadro_em_progresso, text="Em progresso",width=26, height=3, font=fonte, bg=cor_em_progresso,borderwidth=2,relief=tk.SOLID)
label_em_progresso.pack()
label_concluido = tk.Label(quadro_concluido, text="Concluído",width=26, height=3, font=fonte, bg=cor_concluido,borderwidth=2,relief=tk.SOLID)
label_concluido.pack()

# Cria as listas em cada coluna
lista_a_fazer = tk.Listbox(quadro_a_fazer, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_a_fazer.pack()
lista_em_progresso = tk.Listbox(quadro_em_progresso, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_em_progresso.pack()
lista_concluido = tk.Listbox(quadro_concluido, selectbackground='#ADD8E6', selectmode=tk.SINGLE, width=24, height=14, font=fonte)
lista_concluido.pack()

# Cria um caixa de entrade de texto para escrever tarefas 
escrevaTarefa = tk.Label(text="Escreva abaixo a sua tarefa, após clique em 'Adicionar Tarefa' :",font=fonte)
escrevaTarefa.pack(pady=5)
quadro_superior = tk.Frame(janela, bg=cor_fundo)
quadro_superior.pack(pady=20)
entrada = tk.Entry(quadro_superior, width=40, font=fonte)
entrada.pack()


def adicionar_tarefa():
  nova_tarefa = entrada.get()
  if nova_tarefa:
    lista_a_fazer.insert(tk.END, nova_tarefa)
    entrada.delete(0, tk.END)
  else:
    messagebox.showwarning("Aviso", "Digite uma tarefa válida!")

# Inicia a interface gráfica
janela.mainloop()
