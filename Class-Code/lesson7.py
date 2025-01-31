import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")

tasks = []
completed_status = []

# Function to update the listbox with tasks and their status
def update_listbox():
    task_listbox.delete(0, tk.END)  # Clear the current contents of the listbox

    for index, task in enumerate(tasks):
        status = "(completed)" if completed_status[index] else "(uncompleted)"
        task_listbox.insert(tk.END, f"{index + 1}. {task} {status}")

    update_status_labels()  # Update the status labels showing completed and uncompleted tasks

# Function to update the status labels for completed and uncompleted tasks
def update_status_labels():
    completed_count = sum(completed_status)
    uncompleted_count = len(tasks) - completed_count

    # Update the labels with the counts
    completed_label.config(text=f"Completed Tasks: {completed_count}")
    uncompleted_label.config(text=f"Uncompleted Tasks: {uncompleted_count}")

def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        completed_status.append(False)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        del tasks[selected_task_index]  # Remove the selected task from the tasks list
        del completed_status[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to mark the selected task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        completed_status[selected_task_index] = True  # Mark the task as completed
        update_listbox()  # Update the listbox to reflect the changes
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")  # Show a warning if no task is selected

# GUI STUFF
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons to add tasks
add_tasks_button = tk.Button(root, text="Add Tasks", command=add_task)
add_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Button to remove tasks
remove_tasks_button = tk.Button(root, text="Remove Task", command=remove_task)  # Create a Button to remove tasks
remove_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Button to mark tasks as completed
mark_tasks_button = tk.Button(root, text="Mark Task as Completed", command=mark_task_completed)  # Create a Button to mark tasks as completed
mark_tasks_button.pack(pady=5)  # Add the Button to the window with padding

# Listbox to display the tasks
task_listbox = tk.Listbox(root, width=50, height=15)  # Create a Listbox widget to show tasks
task_listbox.pack(pady=10)  # Add the Listbox to the window with padding


# Labels to display the number of completed and uncompleted tasks
completed_label = tk.Label(root, text="Completed Tasks: 0")  # Create a Label to show completed tasks count
completed_label.pack()  # Add the Label to the window

# Label to display the number of uncompleted tasks
uncompleted_label = tk.Label(root, text="Uncompleted Tasks: 0")  # Create a Label to show uncompleted tasks count
uncompleted_label.pack()  # Add the Label to the window

# Start the main event loop
root.mainloop()  # Run the Tkinter event loop to display the window and handle user interactions
