import tkinter as tk
from tkinter import *

contatos = []

janelaPrincipal = tk.Tk()

# Propriedades da janela
janelaPrincipal.title("Lista Telefônica")
janelaPrincipal["background"] = "white"
# Largura x Altura + distância Esquerda + distância Topo
janelaPrincipal.geometry("600x400+500+200")
janelaPrincipal.resizable(0, 0)

frame_q1 = Frame(
    janelaPrincipal, borderwidth=1, relief='solid', background='black')
frame_q1.place(x=10, y=10, width=580, height=380)

titulo = Label(janelaPrincipal, text="LISTA TELEFÔNICA",
               background='black', foreground='white', font="Arial 12")
titulo.pack(pady=30, side=TOP)

# Caixas de entrada de informação
ver_contatos = Button(janelaPrincipal, text='Abrir Agenda', width=15,
                      command=lambda: abrirAgenda())
ver_contatos.pack(pady=15, side=TOP)

inserir_contato = Button(janelaPrincipal, text='Inserir Contato', width=15,
                         command=lambda: inserirContato())
inserir_contato.pack(pady=15, side=TOP)

excluir_contato = Button(janelaPrincipal, text='Excluir Contato', width=15,
                         command=lambda: excluirContato())
excluir_contato.pack(pady=15, side=TOP)


def abrirAgenda():
    janelaAgenda = tk.Tk()

    # Propriedades da janela
    janelaAgenda.title("Lista Telefônica")
    janelaAgenda["background"] = "white"
    # Largura x Altura + distância Esquerda + distância Topo
    janelaAgenda.geometry("600x400+500+200")
    janelaAgenda.resizable(0, 0)

    frame_q1 = Frame(
        janelaAgenda, borderwidth=1, relief='solid', background='black')
    frame_q1.place(x=10, y=10, width=580, height=380)

    titulo = Label(janelaAgenda, text="CONTATOS",
                   background='black', foreground='white', font="Arial 12")
    titulo.pack(pady=30, side=TOP)

    if contatos == "":
        mensagem = Label(janelaAgenda, text="Agenda Vazia",
                         background='black', foreground='white', font="Arial 12")
        mensagem.pack(pady=30, side=TOP)

    janelaAgenda.mainloop()


def inserirContato():
    janelaInserir = tk.Tk()

    # Propriedades da janela
    janelaInserir.title("Lista Telefônica")
    janelaInserir["background"] = "white"
    # Largura x Altura + distância Esquerda + distância Topo
    janelaInserir.geometry("600x400+500+200")
    janelaInserir.resizable(0, 0)

    frame_q1 = Frame(
        janelaInserir, borderwidth=1, relief='solid', background='black')
    frame_q1.place(x=10, y=10, width=580, height=380)

    titulo = Label(janelaInserir, text="INSERIR CONTATO",
                   background='black', foreground='white', font="Arial 12")
    titulo.pack(pady=30, side=TOP)

    # Caixas de entrada de informação
    stringNome = StringVar(value='Nome Completo')
    nome = Entry(janelaInserir, width=30, textvariable=stringNome)
    nome.pack(pady=15, side=TOP)

    stringEndereco = StringVar(value='Endereço')
    endereco = Entry(janelaInserir, width=30, textvariable=stringEndereco)
    endereco.pack(pady=15, side=TOP)

    stringTelefone = StringVar(value='Telefone')
    telefone = Entry(janelaInserir, width=30, textvariable=stringTelefone)
    telefone.pack(pady=15, side=TOP)

    stringEmail = StringVar(value='Email')
    email = Entry(janelaInserir, width=30, textvariable=stringEmail)
    email.pack(pady=15, side=TOP)

    inserir = Button(janelaInserir, text='Inserir',
                     command=lambda: enviarFormulario())
    inserir.pack(pady=25, side=TOP)

    def enviarFormulario():
        contato = [nome.get(), endereco.get(),
                   telefone.get(), email.get()]
        contatos.append(contato)
        print(contatos)

    janelaInserir.mainloop()


janelaPrincipal.mainloop()
