import tkinter as tk

def createTask():
    newTask = entryField.get()
    listboxField.insert(0, newTask)

root = tk.Tk()
root.geometry("500x400")
root.title("ToDoList")

entryField = tk.Entry()
entryField.pack(anchor="n", padx=5, fill="x", pady=5)

button = tk.Button(text="New task", borderwidth=1, wraplength=50, command=createTask)
button.pack(fill="y", pady=5, side="right")

listboxField = tk.Listbox()
listboxField.pack()

root.mainloop()

