import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror



def createTask():
    if entryField.get().isspace() or entryField.get() == "":
        showerror("Ошибка ввода!", "Вы не ввели новую задачу!")
    else:
        newTask = entryField.get().strip()
        listboxField.insert(0, newTask)

def deleteTask():
    selectTask = listboxField.curselection()
    if not listboxField.curselection() and listboxField.size() > 0:
        showerror("Ошибка выбора!", "Выбери задачу для удаления")
    elif listboxField.size() == 0:
        showerror("Ошибка ввода!", "Ваш список задач пуст!")
    else:
        listboxField.delete(selectTask)

root = tk.Tk()
root.geometry("500x400")
root.title("ToDoList")

frame = ttk.Frame(borderwidth=1, relief="solid")

entryField = tk.Entry()
entryField.pack(anchor="n", padx=5, fill="x", pady=5)

buttonCreate = ttk.Button(frame, text="New task", command=createTask)
buttonCreate.pack(fill="x", pady=1, anchor="n", ipady=1, padx=5)

buttonDelete = ttk.Button(frame, text="Delete task", command=deleteTask)
buttonDelete.pack(fill="x", pady=1, anchor="n", ipady=1, padx=5)

frame.pack(fill="x", pady=2, anchor="n", padx=5)

listboxField = tk.Listbox(root, bg="gainsboro", fg="SlateBlue1")
listboxField.pack(fill="both", pady=5, padx=5, expand=True)

root.mainloop()

