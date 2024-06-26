import datetime
import tkinter as tk
from tkinter import ttk


#Вывод на экран

def read_file():
    with open('zametki.csv', 'r') as f:
        data = f.read()
        display = tk.Toplevel()
        display.title("Заметки")
        display.geometry("500x500")

        for i, line in enumerate(data.split('\n\n')):
            if line == '\n':
                i += 1
            text = tk.Text(display)
            text.config(width=40, height=5)
            text.pack(fill="both")
            text.insert('1.0', line.strip()) 
            bt = ttk.Button(display, text="Редактировать")
            bt.pack(fill="both")


#Создание заметки
def create_file():
    def save_file():
        with open('zametki.csv', 'a') as f:

            # Получаем текущую дату и время
            time = datetime.datetime.now()
            # Форматируем дату и время в определенный формат
            timered = time.strftime("%Y-%m-%d %H:%M:%S")

            text = f"{timered}\n {insert.get()}\n\n"
            f.write(text)
            window.destroy()

    window = tk.Tk()
    window.title("Запись в файл")
    window.geometry("300x200")

    insert = ttk.Entry(window)
    #insert.config(width=40, height=10)
    insert.pack(fill="both")

    save_button = ttk.Button(window, text="Сохранить в файл", command=save_file)
    save_button.pack()




