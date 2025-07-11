import tkinter as tk
from tkinter import ttk, Variable
from tkinter.messagebox import showerror

with open("saveInfo.txt", "r") as File:

    def createTask():
        if entryField.get().isspace() or entryField.get() == "":
            showerror("Ошибка ввода!", "Вы не ввели новую задачу!")
        else:
            newTask = entryField.get().strip()
            listboxField.insert(0, newTask)
            with open("saveInfo.txt", "a") as File:
                print(entryField.get().strip(), file=File)


    def deleteTask():
        selectTask = listboxField.curselection()
        if not listboxField.curselection() and listboxField.size() > 0:
            showerror("Ошибка выбора!", "Выбери задачу для удаления")
        elif listboxField.size() == 0:
            showerror("Ошибка ввода!", "Ваш список задач пуст!")
        else:
            listboxField.delete(selectTask)
            with open("saveInfo.txt", "w+") as File:
                allWritedTasks = list(listboxField.get(0, listboxField.size()))
                File.writelines([f"{x}\n" for x in allWritedTasks])

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

    tasks = [task.strip() for task in File.readlines()]
    tasks_var = Variable(value=tasks)
    listboxField = tk.Listbox(root, bg="gainsboro", fg="SlateBlue1", listvariable=tasks_var)
    listboxField.pack(fill="both", pady=5, padx=5, expand=True)

    root.mainloop()

