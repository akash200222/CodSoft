import tkinter
import tkinter.messagebox

wind = tkinter.Tk()
wind.title("To Do List")

def task_adding():
    todo = task_add.get()
    if todo != "":
        box.insert(tkinter.END, (todo, False))  
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention", message="Please add a task")

def task_delete():
    try:
        index_todo = box.curselection()[0]
        box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention", message="To delete a task, you must select a task")

def task_select():
    try:
        index_todo = box.curselection()[0]
        task = box.get(index_todo)
        new_task = (task[0], not task[1])  
        box.delete(index_todo)
        box.insert(index_todo, new_task)
    except:
        tkinter.messagebox.showwarning(title="Attention", message="To select a task, you must select a task")

frame = tkinter.Frame(wind)
frame.pack()

box = tkinter.Listbox(frame, height=20, width=50)
box.pack(side=tkinter.LEFT)

scrol = tkinter.Scrollbar(frame)
scrol.pack(side=tkinter.RIGHT, fill=tkinter.Y)

box.config(yscrollcommand=scrol.set)
scrol.config(command=box.yview)

task_add = tkinter.Entry(wind, width=70)
task_add.pack()

task_add_button = tkinter.Button(wind, text="Click to add task", font=("arial", 20, "bold"), background="orange", width=40, command=task_adding)
task_add_button.pack()

task_delete_button = tkinter.Button(wind, text="Click to delete task", font=("arial", 20, "bold"), background="white", width=40, command=task_delete)
task_delete_button.pack()



wind.mainloop()