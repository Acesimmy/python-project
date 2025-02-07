from tkinter import *
from tkinter import messagebox

app = Tk()
app.title("Task hai")
app.geometry("500x500")


def add_task():
    task = entry_task.get()
    tasks.append(task)
    update_task_list()


def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        update_task_list()


def update_task_list():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

tasks = []

label_task = Label(app, text="Task")
label_task.pack()

entry_task = Entry(app)
entry_task.pack()

btn_add = Button(app, text="Add", command=add_task)
btn_add.pack()

btn_delete = Button(app, text="Delete", command=delete_task)
btn_delete.pack()

task_listbox = Listbox(app)
task_listbox.pack()

app.mainloop()