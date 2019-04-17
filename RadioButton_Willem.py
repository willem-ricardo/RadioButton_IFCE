import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Select your pet !")

rbtSelect = tk.IntVar()
rbtSelect.set(1)

imgPapagaio = tk.PhotoImage(file="Bird.gif")
imgGato = tk.PhotoImage(file="Cat.gif")
imgCachorro = tk.PhotoImage(file="Dog.gif")
imgPorco = tk.PhotoImage(file="Rabbit.gif")
imgCoelho = tk.PhotoImage(file="Rabbit.gif")


### Comando para trocar image
def mudar_figura():
    if rbtSelect.get() == 1:
        tela.create_image(66, 66, image=imgPapagaio)
    elif rbtSelect.get() == 2:
        tela.create_image(66, 66, image=imgGato)
    elif rbtSelect.get() == 3:
        tela.create_image(66, 66, image=imgCachorro)
    elif rbtSelect.get() == 4:
        tela.create_image(66, 66, image=imgPorco)
    elif rbtSelect.get() == 5:
        tela.create_image(66, 66, image=imgCoelho)


### Estrutura do radio button
rbtBird = ttk.Radiobutton(win, text='Papagaio', width=9, value=1, variable=rbtSelect, command=mudar_figura)
rbtBird.grid(column=0, row=0, padx=5)
rbtCat = ttk.Radiobutton(win, text='Gato', width=9, value=2, variable=rbtSelect, command=mudar_figura)
rbtCat.grid(column=0, row=1)
rbtDog = ttk.Radiobutton(win, text='Cachorro', width=9, value=3, variable=rbtSelect, command=mudar_figura)
rbtDog.grid(column=0, row=2)
rbtPig = ttk.Radiobutton(win, text='Porco', width=9, value=4, variable=rbtSelect, command=mudar_figura)
rbtPig.grid(column=0, row=3)
rbtRabbit = ttk.Radiobutton(win, text='Coelho', width=9, value=5, variable=rbtSelect, command=mudar_figura)
rbtRabbit.grid(column=0, row=4)


### Criando o canvas onde as imagens serão apresentadas
tela = tk.Canvas(win, width=129, height=129, bg="blue")
tela.create_image(66, 66, image=imgPapagaio)
tela.grid(column=1, row=0, rowspan=5)

win.resizable(0,0)
win.mainloop()
