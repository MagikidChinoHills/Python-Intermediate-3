port tkinter as tk
from tkinter import messagebox

# Initialize main window
app = tk.Tk()
app.title("Task Manager")
app.geometry("500x400")

task_list = []
task_status = []

def refresh_list():
    """Update the Listbox with current tasks and their status."""
    task_display.delete(0, tk.END)
    
    for i, task in enumerate(task_list):
        status_text = "(Completed)" if task_status[i] else "(Pending)"
        task_display.insert(tk.END, f"{i + 1}. {task} {status_text}")
    
    refresh_status_labels()
im
def refresh_status_labels():
    """Update the labels displaying task statistics."""
    completed_tasks = sum(task_status)
    pending_tasks = len(task_list) - completed_tasks
    
    completed_count_label.config(text=f"Completed Tasks: {completed_tasks}")
    pending_count_label.config(text=f"Pending Tasks: {pending_tasks}")

def add_new_task():
    """Add a new task to the list."""
    new_task = task_input.get().strip()
    
    if new_task:
        task_list.append(new_task)
        task_status.append(False)
        refresh_list()
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    """Remove the selected task from the list."""
    try:
        selected_index = task_display.curselection()[0]
        del task_list[selected_index]
        del task_status[selected_index]
        refresh_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def complete_task():
    """Mark a selected task as completed."""
    try:
        selected_index = task_display.curselection()[0]
        task_status[selected_index] = True
        refresh_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Input field for task entry
task_input = tk.Entry(app, width=40)
task_input.pack(pady=10)

# Buttons for task operations
add_button = tk.Button(app, text="Add Task", command=add_new_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Remove Task", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(app, text="Mark as Completed", command=complete_task)
complete_button.pack(pady=10)

# Labels to display task counts
completed_count_label = tk.Label(app, text="Completed Tasks: 0")
completed_count_label.pack()

pending_count_label = tk.Label(app, text="Pending Tasks: 0")
pending_count_label.pack()

# Listbox to display tasks
task_display = tk.Listbox(app, width=50, height=15)
task_display.pack(pady=10)

# Run the application
app.mainloop()
