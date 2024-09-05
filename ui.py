from tkinter import N, Tk, TkVersion, ttk
import tkinter
from logger import create_file, read_file

def Interface():
    root = Tk()
    root.title("Приложение заметки")
    root.geometry("400x400")

    lable = ttk.Label(root, text="Выберите действие", anchor=N)
    lable.pack()

    load_bt = tkinter.Button(root, text="Показать заметки", command=read_file)
    load_bt.pack(fill="both")
    bt2 = tkinter.Button(root, text="Создать заметку", command=create_file)
    bt2.pack(fill="both")

    root.mainloop()