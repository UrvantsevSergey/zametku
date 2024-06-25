import datetime
import tkinter as tk
from tkinter import ttk
import uuid

#Вывод на экран
def read_file():
    with open('zametki.csv', 'r') as f:
        data = f.read()  
        display = tk.Toplevel()
        display.title("Заметки")
        display.geometry("300x200")
        text = tk.Text(display)
        text.pack()
        text.insert('1.0', data) 

#Создание заметки
def create_file():
    def save_file():
        with open('zametki.csv', 'a') as f:
            text = f"{insert.get()}" + "\n"
            f.write(text)
            window.destroy()

    window = tk.Tk()
    window.title("Запись в файл")
    window.geometry("300x200")

    insert = ttk.Entry(window)
    insert.pack()

    save_button = ttk.Button(window, text="Сохранить в файл", command=save_file)
    save_button.pack()




