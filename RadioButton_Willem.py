import tkinter as tk
from tkinter import ttk

win tk.Tk()
win.title("Select your pet !")

rbtSelect = tk.IntVar()
rbtSelect.set(1)

imgPapagaio = tk.PhotoImage(file="Bird.gif")
imgGato = tk.PhotoImage(file="Cat.git")
imgCachorro = tk.PhotoImage(file="Dog.git")
imgPorco = tk.PhotoImage(file="Rabbit.git")
imgCoelho = tk.PhotoImage(file="Rabbit.git")


### Estrutura do radio button
rbtBird = ttk.Radiobutton(win, text='Papagaio', width=9, value=1, variable=rbtSelect, command=mudar_figura)
rbtBird.grid(columm=0, row=0, padx=5)
rbtCat = ttk.Radiobutton(win, text='Gato', width=9, value=2, variable=rbtSelect, command=mudar_figura)
rbtCat.grid(columm=0, row=1, padx=5)
rbtDog = ttk.Radiobutton(win, text='Cachorro', width=9, value=3, variable=rbtSelect, command=mudar_figura)
rbtDog.grid(columm=0, row=2, padx=5)
rbtPig = ttk.Radiobutton(win, text='Porco', width=9, value=4, variable=rbtSelect, command=mudar_figura)
rbtPig.grid(columm=0, row=3, padx=5)
rbtRabit = ttk.Radiobutton(win, text='Coelho', width=9, value=5, variable=rbtSelect, command=mudar_figura)
rbtRabbit.grid(columm=0, row=4, padx=5)
