# Угадай цвет светофора
import tkinter as tk
import random
from tkinter import messagebox as mb

# from gevent.libev.watcher import check


def check():
    colors=["зеленый","красный","желтый"]
    computer = random.choice(colors)
    user = e.get().lower()
    if computer == user:
        mb.showinfo("Результат","Вы угадали")
    else:
        mb.showinfo(f"Результат",f"Вы не угадали\n компьютер  выбрал {computer}")




win = tk.Tk()
win.geometry ("500x300+200+100")
win.title ("Угадай цвет светофора")

l = tk.Label(win, text = "Введите цвет светофора!")
l.pack(pady = 10)
e=tk.Entry(win, width = 30)
e.pack(pady = 10)

b = tk.Button(win, text = "Проверить", command= check)
b.pack(pady = 10)


win.mainloop()