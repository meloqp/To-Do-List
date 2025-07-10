import tkinter as tk
from tkinter import ttk

def createTask():
    newTask = entryField.get()
    listboxField.insert(0, newTask)

def deleteTask():
    pass

root = tk.Tk()
root.geometry("500x400")
root.title("ToDoList")

entryField = tk.Entry()
entryField.pack(anchor="n", padx=5, fill="x", pady=5)

buttonCreate = ttk.Button(text="New task", command=createTask)
buttonCreate.pack(fill="x", pady=1, anchor="n", ipady=1, padx=5)

buttonDelete = ttk.Button(text="Delete task", command=deleteTask)
buttonDelete.pack(fill="x", pady=2, anchor="n")

listboxField = tk.Listbox(root, bg="gainsboro")
listboxField.pack(fill="both", pady=5, padx=5, expand=True)

root.mainloop()

