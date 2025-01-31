import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-do List")
root.geometry("500x400")

tasks = []
completed_status = []

def update_listbox():
    task_listbox.delete(0, tk.END)

    for index, task in enumerate(tasks):
        status = "(completed)" if completed_status[index] else "(uncompleted)"
        task_listbox.insert(tk.END, f"{index + 1}. {task} {status}")

    update_status_labels()


def update_status_labels():
    completed_count = sum(completed_status)
    uncompleted_count = len(tasks) - completed_count

    completed_label.config(task=f"Completed Tasks: {completed_count}")#-
    uncompleted_label.config(text=f"Uncompleted Task: {uncompleted_count}")#-
    completed_label.config(text=f"Completed Tasks: {completed_count}")#+
    uncompleted_label.config(text=f"Uncompleted Tasks: {uncompleted_count}")#+


def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        completed_status.append(False)
        update_listbox()
        task_entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Warning," "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        del completed_status[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        completed_status[selected_task_index] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")
    
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

mark_tasks_button = tk.Button(root, text="Mark Task as Completed", command=mark_task_completed)
mark_tasks_button.pack(pady=10)

completed_label = tk.Label(root, text="Completed Tasks: 0")
completed_label.pack()

uncompleted_label = tk.Label(root, text="Uncompleted Tasks: 0")
uncompleted_label.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()