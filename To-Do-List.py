import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

# Function to mark task as done (crossed)
def mark_done():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_index)
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(tk.END, f"✔ {task_text}")
    except IndexError:
        messagebox.showwarning("Mark Error", "Please select a task to mark as done.")

# Main GUI window
window = tk.Tk()
window.title("Simple To-Do List")
window.geometry("400x400")
window.config(bg="Sky Blue")

# Entry widget
entry_task = tk.Entry(window, width=35, font=("Arial", 12))
entry_task.pack(pady=10)

# Add button
button_add = tk.Button(window, text="Add Task", width=15, command=add_task, bg="Light Green")
button_add.pack(pady=5)

# Listbox to display tasks
listbox_tasks = tk.Listbox(window, width=40, height=10, font=("Arial", 12), selectbackground="Green")
listbox_tasks.pack(pady=10)

# Done and Delete buttons
button_done = tk.Button(window, text="Mark as Done", width=15, command=mark_done, bg="Yellow")
button_done.pack(pady=5)

button_delete = tk.Button(window, text="Delete Task", width=15, command=delete_task, bg="Red")
button_delete.pack(pady=5)

# Run the application
window.mainloop()