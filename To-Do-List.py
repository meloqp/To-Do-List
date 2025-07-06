import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("ToDoList")
button = tk.Button(text="Create task")
button.pack(fill="x", padx=30)
root.mainloop()