# todo_app_gui.py
# GUI To-Do List App using Tkinter

import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = listbox.get(index)
        listbox.delete(index)
        tasks.remove(task)
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()

root = tk.Tk()
root.title("📝 Python To-Do List")
root.geometry("300x400")

title = tk.Label(root, text="To-Do List", font=("Arial", 30, "bold"))
title.pack(pady=30)

entry = tk.Entry(root, width=40)
entry.pack(pady=20)

tk.Button(root, text="Add Task", width=15, command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All", width=15, command=clear_tasks).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)

root.mainloop()
